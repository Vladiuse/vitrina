from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index,name='products'),

    path('product/<slug:product_slug>', views.product_details, name='product_detail'),
    path('leads', views.leads, name='leads'),
    path('success/<str:lead_id>', views.success, name='success'),
    path('policy', views.policy, name='policy'),

    path('<slug:cat_slug>', views.category, name='category'),

    path('product-next-prev/<str:direction>/<str:curr_id>', views.prev_next_product, name='prev_next_product'),
]