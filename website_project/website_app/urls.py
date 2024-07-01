from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import*

from django.urls import path
from .views import order_view

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('order/', views.order_view, name='order'),
    path('order_success/', views.order_success, name='order_success'),
    path('home', views.home, name='home'),
]






