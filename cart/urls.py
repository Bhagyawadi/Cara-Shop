from django.urls import path
from .import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('shop/' , views.shop , name='shop'),
    path('products/<int:myid>' , views.products , name='products'),
    path('blog/' , views.blog , name='blog'),
    path('about/' , views.about , name='about'),
    path('checkout/' , views.checkout , name='checkout'),
    path('tracker/' , views.tracker , name='tracker'),
    path('contact/' , views.contact , name='contact'),
    path('cart/' , views.cart , name='cart'),
]
