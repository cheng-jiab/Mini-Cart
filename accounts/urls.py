from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/<uidb64>/<token>', views.resetPassword, name='resetPassword'),
    path('resetPasswordPage/', views.resetPasswordPage, name='resetPasswordPage'),
]
