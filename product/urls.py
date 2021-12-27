from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('cutomer_create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('order_create/', views.OrderCreateView.as_view(), name='order_create'),

]
