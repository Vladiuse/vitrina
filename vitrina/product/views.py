from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Offer, Lead, Category
from .forms import LeadForm
from django.contrib.auth.decorators import login_required

RANDOM_PRODUCT_COUNT = 3
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def index(requests):
    products = Offer.published.select_related('category').all().order_by('-pk')
    content = {
        'products': products,
    }
    return render(requests, 'product/products.html', content)

def category(requests, cat_slug):
    category = Category.objects.get(slug=cat_slug)
    products = Offer.objects.filter(category=category)
    content = {
        'products': products,
        'category': category,
    }
    return render(requests, 'product/category_products.html', content)



def product_details(requests, product_slug):
    product = Offer.objects.get(slug=product_slug)
    random_products = Offer.objects.exclude(pk=product.pk).order_by('?')
    if not product.mini_land:
        product.mini_land = 'default'
    if requests.method == 'POST':
        lead_form = LeadForm(requests.POST)
        if lead_form.is_valid():
            lead = lead_form.save()
            lead.send()
            return HttpResponseRedirect(reverse('product:success', kwargs={'lead_id': lead.id}))
        else:
            # return HttpResponse('Error form')
            content = {
                'form': lead_form,
                'product': product,
                'products': random_products[:RANDOM_PRODUCT_COUNT],
                'client_ip': get_client_ip(requests)
            }
            return render(requests, f'product/mini_lands/{product.mini_land}.html', content)
    else:
        form = LeadForm(initial={'ip':get_client_ip(requests), 'offer': product})
        content = {
            'form': form,
            'product': product,
            'products': random_products[:RANDOM_PRODUCT_COUNT],
            'client_ip': get_client_ip(requests)
        }
        return render(requests, f'product/mini_lands/{product.mini_land}.html', content)

@login_required
def leads(requests):
    leads = Lead.objects.all().order_by('-pk')
    content = {
        'leads': leads,
    }
    return render(requests, 'product/leads.html', content)


def success(requests, lead_id):
    lead = get_object_or_404(Lead,pk=lead_id)
    random_products = Offer.objects.order_by('?')
    # lead = Lead.objects.get(pk=lead_id)
    content = {
        'lead': lead,
        'products': random_products[:RANDOM_PRODUCT_COUNT],
    }
    return render(requests, 'product/success.html', content)


def prev_next_product(requests,direction, curr_id):
    curr_id = int(curr_id)
    if direction == 'prev':
        product_slug = Offer.get_prev(curr_id)
    else:
        product_slug = Offer.get_next(curr_id)
    return HttpResponseRedirect(reverse('product:product_detail', kwargs={'product_slug': product_slug}))


# def error_404(request,exception):
#     return render(request,'404.html')