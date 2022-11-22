from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Offer, Lead, Category
from .forms import LeadForm


def index(requests):
    products = Offer.published.all()
    content = {
        'products': products,
    }
    return render(requests, 'product/products.html', content)

def category(requests, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    products = Offer.objects.filter(category=category)
    content = {
        'products': products,
        'category': category,
    }
    return render(requests, 'product/category_products.html', content)



def product_details(requests, product_id):
    RANDOM_PRODUCT_COUNT = 3
    if requests.method == 'POST':
        lead_form = LeadForm(requests.POST)
        if lead_form.is_valid:
            lead = lead_form.save()
            lead.send()
            return HttpResponseRedirect(reverse('product:success', kwargs={'lead_id': lead.id}))
        else:
            return HttpResponse('Error form')
    else:
        product = Offer.objects.get(pk=product_id)
        random_products = Offer.objects.exclude(pk=product_id).order_by('?')

        content = {
            'product': product,
            'products': random_products[:RANDOM_PRODUCT_COUNT],
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


def policy(requests):
    return render(requests, 'product/policy.html')

def prev_next_product(requests,direction, curr_id):
    curr_id = int(curr_id)
    if direction == 'prev':
        product_id = Offer.get_prev(curr_id)
    else:
        product_id = Offer.get_next(curr_id)
    return HttpResponseRedirect(reverse('product:product_detail', kwargs={'product_id': product_id}))
