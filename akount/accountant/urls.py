from django.urls import path
from .views import customer_list, sales_invoice_list, purchase_invoice_list

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('sales_invoices/', sales_invoice_list, name='sales_invoice_list'),
    path('purchase_invoices/', purchase_invoice_list, name='purchase_invoice_list'),
]
