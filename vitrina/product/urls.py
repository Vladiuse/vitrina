from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index,name='products'),
    path('product/<str:product_id>', views.product_details, name='product_detail'),
    path('leads', views.leads, name='leads'),
    path('success/<str:lead_id>', views.success, name='success'),
]