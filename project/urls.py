"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app1.views import CategoryView, CategoryAddView, SizeView, SizeAddView, ProductView, ProductAddView, \
    ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', CategoryView.as_view(), name='category'),
    path('category_add/', CategoryAddView.as_view(), name='category_add'),
    path('size/', SizeView.as_view(), name='size'),
    path('size_add/', SizeAddView.as_view(), name='size_add'),
    path('product/', ProductView.as_view(), name='product'),
    path('product_add/', ProductAddView.as_view(), name='product_add'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_add'),


]
