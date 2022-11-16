from django.shortcuts import render
from django.http import HttpResponse
from .models import Offer, Lead
from .forms import LeadForm

def index(requests):
    products = Offer.objects.all()
    content = {
        'products': products,
    }
    return render(requests, 'product/products.html', content)

def product_details(requests, product_id):
    if requests.method == 'POST':
        lead_form = LeadForm(requests.POST)
        if lead_form.is_valid:
            lead_form.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Error form')
    else:
        product = Offer.objects.get(pk=product_id)
        content = {
            'product': product,
        }
        return render(requests, 'product/product_detail.html', content)


def leads(requests):
    leads = Lead.objects.all()
    content = {
        'leads': leads,
    }
    return render(requests, 'product/leads.html', content)
