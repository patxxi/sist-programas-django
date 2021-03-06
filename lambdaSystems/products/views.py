# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

# Forms
from products.forms import ProductForm, CategoryForm

from products.models import Products


class CreateProductView(LoginRequiredMixin, CreateView):
    """Create a Product using the ProductForm"""
    template_name = "products/create_product.html"
    form_class = ProductForm
    # TODO
    success_url = reverse_lazy('products:newproduct')

class CreateCategoryView(LoginRequiredMixin, CreateView):
    """Create a Category Using thee CategoryForm"""
    template_name = "products/create_category.html"
    form_class = CategoryForm
    # TODO
    success_url = reverse_lazy('products:newproduct')

class ProductsFeedView(LoginRequiredMixin, ListView):
    """List All Products registered"""

    # Not Tested Or Finished
    template_name = "products/product_feed.html"
    ordering = ["name",]
    model = Products
    context_object_name = 'products'
    paginate_by = 30
