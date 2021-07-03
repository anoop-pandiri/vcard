from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('payment-status/', views.payment_status, name='payment-status'),
]