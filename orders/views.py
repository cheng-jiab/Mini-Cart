from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
from .models import Order, OrderProduct
from store.models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
import datetime
import decimal


def payments(request):
    order = Order.objects.filter(user=request.user, isOrdered=False).order_by('-createdAt')[0]
    cartItems = CartItem.objects.filter(user=request.user)
    for item in cartItems:
         # Move the cart items to order product
        orderProduct = OrderProduct()
        orderProduct.order_id = order.id
        orderProduct.user_id = request.user.id
        orderProduct.product_id = item.product.id
        orderProduct.variations_id = item.variation.id
        orderProduct.quantity = item.quantity
        orderProduct.productPrice = item.product.price
        orderProduct.isOrdered = True
        orderProduct.save()

        # Reduce the quantity of the sold product
        product = Product.objects.get(id=item.product.id)
        product.stock -= item.quantity

    order.status = 'Confirmed'
    order.isOrdered = True
    order.save()
    # clear cart
    CartItem.objects.filter(user=request.user).delete()
    
    # send confirmation email to customer
    mailSubject = 'Thank you for your order!'
     
    message = render_to_string('orders/orderConfirmationEmail.html', {
        'user': request.user,
        'order': order,
    } )
    toEmail = request.user.email
    #sendEmail = EmailMessage(mailSubject, message, to=[toEmail])
    #sendEmail.send()

    messages.success(request, 'Order confirmation email has been sent!')
    # redirect to thank you page
    
    return redirect(reverse('orderComplete', args=[order.id]))

# Create your views here.
def placeOrder(request):
    user = request.user
    cartItems = CartItem.objects.filter(user=user)
    cartCount = cartItems.count()
    if cartCount <= 0:
        return redirect('store')
    
    tax , quantity, total, totalAfterTax = 0, 0, 0, 0
    for cartItem in cartItems:
        #total += (cartItem.product.price * cartItem.quantity)
        total += cartItem.subtotal()
        quantity += cartItem.quantity

    tax = round(decimal.Decimal(0.07) * total,2)
    totalAfterTax = total + tax

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = user
            data.firstName = form.cleaned_data['firstName']
            data.lastName = form.cleaned_data['lastName']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.addressLine1 = form.cleaned_data['addressLine1']
            data.addressLine2 = form.cleaned_data['addressLine2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.orderNote = form.cleaned_data['orderNote']
            data.orderTotal = totalAfterTax
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            #generate order number
            date = datetime.date.today().strftime('%Y%m%d')
            print(data.id)
            orderNumber = date + str(data.id)
            data.orderNumber = orderNumber
            data.save()
            return redirect('payments')
    else:
        return redirect('chekcout')

    
def orderComplete(request, orderId):
    
    order = Order.objects.get(id = orderId)
    orderProducts = OrderProduct.objects.filter(order_id=order.id)
    totalBeforeTax = 0
    for item in orderProducts:
        
        totalBeforeTax += item.productPrice* decimal.Decimal(item.quantity)

    context = {
        'order': order,
        'orderProducts': orderProducts,
        'totalBeforeTax': totalBeforeTax,

    }
    return render(request, 'orders/orderComplete.html', context)
