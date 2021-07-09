from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('', CategoriesListView.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('product/create/<int:pk>', ProductCreateView.as_view(), name='product_create'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/details/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('category/update/<int:pk>', UpdateCategoryView.as_view(), name='update_category'),
    path('product/update/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('category/delete/<int:pk>', DeleteCategoryView.as_view(), name='category_delete'),
    path('product/delete/<int:pk>', DeleteProductView.as_view(), name='product_delete'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
