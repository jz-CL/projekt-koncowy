from django.contrib import messages
from django.shortcuts import render, redirect

from django.views import View
from django.core.exceptions import ValidationError

import secrets
from datetime import datetime
# Create your views here.
from app1.forms import CategoryAddForm, SizeAddForm, BrandAddForm, ColorAddForm, ProductAddForm
from app1.models import Category, Size, Product, Color, Brand


# TODO modyfikacja rekordów Category, Size, Product, Color, Brand
# TODO unikalny numer identyfikacyjny
# TODO tablica zestawów kompletowanych towarów

# ------------------------ Category ------------------------

class CategoryView(View):
    template_name = 'app1/category_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        categories = Category.objects.all()
        ctx = {
            'categories': categories,
        }
        return render(request, self.template_name, ctx)

class CategoryAddView(View):
    template_name = 'app1/category_add.html'

    def get(self, request, *args, **kwargs):
        form = CategoryAddForm()

        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = CategoryAddForm(request.POST)
        name = None
        message = None
        if form.is_valid():
            name = form.cleaned_data.get('name')
            kod = form.cleaned_data.get('kod')
            # breakpoint()
            category_len = len(Category.objects.filter(name=name))
            category_kod_len = len(Category.objects.filter(kod=kod))
            if category_len == 0 and category_kod_len == 0:
                category = Category()
                category.name = name
                category.kod = kod
                category.save()

                messages.success(request, 'Dodano nową kategorię.')

                # -> przekieruj na stronę category
                return redirect("category")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                if category_len != 0:
                    message = 'Ta kategoria już jest!'

                if category_kod_len != 0:
                    message = 'Taki kod już istnieje!'
        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
            }
        return render(request, self.template_name, ctx)

# ------------------------ Size ------------------------

class SizeView(View):
    template_name = 'app1/size_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        sizes = Size.objects.all()
        ctx = {
            'sizes': sizes,
        }
        return render(request, self.template_name, ctx)

class SizeAddView(View):
    template_name = 'app1/size_add.html'

    def get(self, request, *args, **kwargs):
        form = SizeAddForm()

        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = SizeAddForm(request.POST)
        name = None
        message = None
        if form.is_valid():
            name = form.cleaned_data.get('name')
            kod = form.cleaned_data.get('kod')
            # breakpoint()
            size_len = len(Size.objects.filter(name=name))
            size_kod_len = len(Size.objects.filter(kod=kod))

            # breakpoint()

            # size.name, size.kod - nie mogą się powtarzać
            if size_len == 0 and size_kod_len == 0:

                size = Size()
                size.name = name
                size.kod = kod
                size.save()

                messages.success(request, 'Dodano nowy rozmiar.')

                # -> przekieruj na stronę size
                return redirect("size")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                if size_len != 0:
                    message = 'Ten rozmiar już jest!'

                if size_kod_len != 0:
                    message = 'Taki kod już istnieje!'

        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
            }
        return render(request, self.template_name, ctx)

class SizeDetailView(View):
    template_name = 'app1/size_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None
        #  404
        size_id = kwargs['pk']

        size = Size.objects.get(pk=size_id)

        ctx = {
            'size': size,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------- Brand -------------------------

class BrandView(View):
    template_name = 'app1/brand_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        brands = Brand.objects.all()
        ctx = {
            'brands': brands,
        }
        return render(request, self.template_name, ctx)

class BrandAddView(View):
    template_name = 'app1/brand_add.html'

    def get(self, request, *args, **kwargs):
        form = BrandAddForm()

        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = BrandAddForm(request.POST)
        name = None
        message = None
        if form.is_valid():
            name = form.cleaned_data.get('name')
            kod = form.cleaned_data.get('kod')
            # breakpoint()
            brand_len = len(Brand.objects.filter(name=name))
            brand_kod_len = len(Brand.objects.filter(kod=kod))

            # breakpoint()

            # size.name, size.kod - nie mogą się powtarzać
            if brand_len == 0 and brand_kod_len == 0:

                brand = Brand()
                brand.name = name
                brand.kod = kod
                brand.save()

                messages.success(request, 'Dodano nowy brand.')

                # -> przekieruj na stronę size
                return redirect("brand")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                if brand_len != 0:
                    message = 'Ten brand już jest!'

                if brand_kod_len != 0:
                    message = 'Taki kod już istnieje!'

        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
            }
        return render(request, self.template_name, ctx)

class BrandDetailView(View):
    template_name = 'app1/brand_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None
        #  404
        brand_id = kwargs['pk']

        brand = Brand.objects.get(pk=brand_id)

        ctx = {
            'brand': brand,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------ Color ------------------------

class ColorView(View):
    template_name = 'app1/color_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        colors = Color.objects.all()
        ctx = {
            'colors': colors,
        }
        return render(request, self.template_name, ctx)

class ColorAddView(View):
    template_name = 'app1/colors_add.html'

    def get(self, request, *args, **kwargs):
        form = ColorAddForm()

        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = ColorAddForm(request.POST)
        name = None
        message = None
        if form.is_valid():
            name = form.cleaned_data.get('name')
            kod = form.cleaned_data.get('kod')
            # breakpoint()
            color_len = len(Color.objects.filter(name=name))
            color_kod_len = len(Color.objects.filter(kod=kod))

            # breakpoint()

            # size.name, size.kod - nie mogą się powtarzać
            if color_len == 0 and color_kod_len == 0:

                color = Color()
                color.name = name
                color.kod = kod
                color.save()

                messages.success(request, 'Dodano nowy kolor.')

                # -> przekieruj na stronę kolor
                return redirect("kolor")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                if color_len != 0:
                    message = 'Ten kolor już jest!'

                if color_kod_len != 0:
                    message = 'Taki kod już istnieje!'

        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
            }
        return render(request, self.template_name, ctx)

class ColorDetailView(View):
    template_name = 'app1/color_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None
        #  404
        color_id = kwargs['pk']

        color = Color.objects.get(pk=color_id)

        ctx = {
            'color': color,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------ Product ------------------------

class ProductView(View):

    template_name = 'app1/product_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        products = Product.objects.all()
        ctx = {
            'products': products,
        }
        return render(request, self.template_name, ctx)

class ProductAddView(View):
    template_name = 'app1/product_add.html'

    def get(self, request, *args, **kwargs):
        form = ProductAddForm()

        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = ProductAddForm(request.POST)
        name = None
        message = None
        if form.is_valid():

            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            current_quantity = form.cleaned_data.get('current_quantity')
            category = form.cleaned_data.get('category')
            size = form.cleaned_data.get('size')
            brand = form.cleaned_data.get('brand')
            color = form.cleaned_data.get('color')



            # breakpoint()
            product_len = len(Product.objects.filter(name=name))
            if product_len == 0:
                product = Product()

                product.name = name
                product.brand = brand
                product.color = color
                product.description = description
                product.price = price
                product.current_quantity = current_quantity
                # breakpoint()
                # product.size = size
                # product.category = category
                # breakpoint()
                # https://docs.python.org/3/library/datetime.html
                # datetime.now().strftime("%Y%m%d%H%M%S%f")
                # https://docs.python.org/3/library/secrets.html
                # import secrets
                #
                # random_string = secrets.token_hex(8)
                product.identifier_exists = brand.kod+category.kod+size.kod
                                            # +datetime.now().strftime("%y%m%d%H%M%S")+name[:3].upper()+'-'+color.kod
                    # (name[:3] + '-' + str(size)).upper() + '-' + secrets.token_hex(8)

                product.save()
                # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
                product.category.add(category)
                product.size.add(size)

                messages.success(request, 'Dodano nowy towar.')

                # -> przekieruj na stronę product
                return redirect("product")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                message = 'Ten towar już jest!'
        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
            }
        return render(request, self.template_name, ctx)

class ProductDetailView(View):
    template_name = 'app1/product_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None
        #  404
        product_id = kwargs['pk']

        product = Product.objects.get(pk=product_id)
        categories = product.category.all()
        ctx = {
            'product': product,
            'categories': categories,
            'message': message
        }

        return render(request, self.template_name, ctx)


# ------------------------ class ------------------------