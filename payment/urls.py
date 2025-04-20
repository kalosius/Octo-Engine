from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_page, name='payment_page'),
    path('pay/', views.initiate_payment, name='initiate_payment'),
    path('payment/confirmation/', views.payment_confirmation, name='payment_confirmation'),
]
