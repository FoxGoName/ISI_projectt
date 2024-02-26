"""
URL configuration for ISI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.cart.views import cart_detail
from apps.core.views import frontpage, contact, about
from apps.store.views import product_detail, category_detail

from apps.core.views import productManagePage

from apps.store.views import productCreateView, editProductView, deleteProductView
from apps.store.api import api_add_to_cart, api_remove_from_cart

# from apps.store.views import productCreateView, editProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('cart/', cart_detail, name='cart'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

    #api
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),

    #projectManager
    path('productManager/', productManagePage, name="productManager"),
    path('productManager/add/', productCreateView.as_view(), name="addProduct"),
    path('productManager/edit/<int:pk>/', editProductView.as_view(), name='editProduct'),
    path('productManager/delete/<int:pk>/', deleteProductView.as_view(), name='deleteProduct'),

    #store
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
