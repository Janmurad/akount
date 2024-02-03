from django.shortcuts import render
from .models import Customer, SalesInvoice, PurchaseInvoice


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accountant/customer_list.html', {'customers': customers})


def sales_invoice_list(request):
    invoices = SalesInvoice.objects.all()
    return render(request, 'accountant/sales_invoice_list.html', {'invoices': invoices})


def purchase_invoice_list(request):
    invoices = PurchaseInvoice.objects.all()
    return render(request, 'accountant/purchase_invoice_list.html', {'invoices': invoices})
