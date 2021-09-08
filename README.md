

# Introduction

The goal of this project is to build a fully custom featured eCommerce application using the Python Django web framework. 

This project is written with django 3.1 and python 3.7, now is deployed on AWS Elastic Beanstalkk with the RDS Postgres databse.

![Default Home View](./screenshots/index.png?raw=true "Title")

### Main Features

* Versatile product options: Using `Product` and `Variance` models enables user to choose different sizes, colors for a single product.
![](./screenshots/details.png?raw=true "Title")

* Product category model: Allow users to filter proudcts based on categories.

* Custom user model: Support features such as email activation, register and login using email address, even the 2-step verification.

* Fully functional shopping cart system: 

    * Can not add the product into cart if it is out of stock.
    * Shopping cart can handle same proudcts with different variations.
    * If user not logged in, shopping cart will be saved based on `request.session_id`
    * When user logs in, items in cart will sync to user's profile automatically.

![](./screenshots/cart.png?raw=true "Title")
* Complete place-order process:
    * Store user's shipping info, generate order number and send out confirmation email.
    * Reduce the quantity of sold proudcts
    * Clear items in the shopping cart.
    

* Bootstrap static files included

* Separated requirements files

### Further Update Plan:
* User dashborad for order trackings.
* Products review system


# Getting Started

### Try deployed application on AWS Beanstalk

[Click here to visit Mini Cart](http://minicart-env.eba-gbn8umgy.us-west-2.elasticbeanstalk.com/)

### Deploy locally
First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/cheng-jiab/Mini-Cart.git
    $ cd Mini-Cart
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver