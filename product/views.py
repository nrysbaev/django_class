from django.shortcuts import render
from . import models, forms
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404


def home_page(request):
    products = models.Product.objects.order_by('-id')
    return render(request, 'product/home_page.html', {'products': products})


class HomePageView(ListView):
    template_name = 'product/home_page.html'
    queryset = models.Product.objects.order_by('-id')

    def get_queryset(self):
        return models.Product.objects.order_by('-id')


class ProductDetailView(DetailView):
    template_name = 'product/product-detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)


class CustomerCreateView(CreateView):
    template_name = 'product/customer-create.html'
    form_class = forms.CustomerForm
    success_url = '..'
    queryset = models.Customer.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class OrderCreateView(CreateView):
    template_name = 'product/order-create.html'
    form_class = forms.OrderForm
    success_url = '..'
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

