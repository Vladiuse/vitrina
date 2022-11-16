from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
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
            lead = lead_form.save()
            print('XXXXXX', lead.pk)
            return HttpResponseRedirect(reverse('product:success', kwargs={'lead_id': lead.id}))
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
    leads = Lead.objects.all().order_by('-pk')
    content = {
        'leads': leads,
    }
    return render(requests, 'product/leads.html', content)

def success(requests, lead_id):
    lead = Lead.objects.get(pk=lead_id)
    content = {
        'lead': lead,
    }
    return render(requests, 'product/success.html', content)
