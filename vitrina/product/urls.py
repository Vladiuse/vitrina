from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index,),
    path('<str:product_id>', views.product_details, name='product_detail'),
]