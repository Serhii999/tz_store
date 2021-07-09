from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


class UserCreateView(CreateView):
    model = StoreUser
    form_class = TzUserForm
    success_url = '/login'
    template_name = 'register.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class CategoriesListView(ListView):
    model = Categories
    template_name = 'main.html'
    login_url = 'login/'
    paginate_by = 5


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = CategoryCreateForm
    success_url = '/'
    permission_required = 'is_superuser'
    template_name = 'categorycreate.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = ProductCreateForm
    success_url = '/'
    permission_required = 'is_superuser'
    template_name = 'productcreate.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.category_id = self.request.POST['category_id']
        return super().form_valid(form=form)


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    login_url = 'login/'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(category=self.request.GET['category_id']).order_by('price')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productdetail.html'


class UpdateCategoryView(PermissionRequiredMixin, UpdateView):
    model = Categories
    permission_required = 'is_superuser'
    login_url = 'login/'
    form_class = CategoryCreateForm
    success_url = '/'
    template_name = 'category_update.html'



class UpdateProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'is_superuser'
    login_url = 'login/'
    form_class = ProductCreateForm
    success_url = '/'
    template_name = 'update_product.html'



class DeleteCategoryView(PermissionRequiredMixin, DeleteView):
    model = Categories
    permission_required = 'is_superuser'
    success_url = '/'


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'is_superuser'
    success_url = '/'



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("main")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')