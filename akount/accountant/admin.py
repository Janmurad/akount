from django.contrib import admin
from .models import Customer, SalesInvoice, PurchaseInvoice


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    # Add more customization options if needed


@admin.register(SalesInvoice)
class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'amount')
    # Add more customization options if needed


@admin.register(PurchaseInvoice)
class PurchaseInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'date', 'amount')
