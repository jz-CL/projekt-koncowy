from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.exceptions import ValidationError

import secrets
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from app1.forms import CategoryAddForm, SizeAddForm, BrandAddForm, \
    ColorAddForm, ProductAddForm #, KlientProductAddForm
from app1.models import Category, Size, Product, \
    Color, Brand, Koszyk


# TODO modyfikacja rekordów Category, Size, Product, Color, Brand
# ToDo jeśli jest dodawany towar a jest już w bazie to stan na magazynie
# TODO tablica zestawów kompletowanych towarów
# Create your views here.

User = get_user_model()

# class DashboardView(PermissionRequiredMixin, View):
class DashboardView(PermissionRequiredMixin, View):
    '''
    zbiorczy widok dostępny do obsługi sklepu
    '''
    template_name = 'app1/dashboard.html'

    # ograniczenie dostępu - użytkownik nie zalogowany
    # login_url = reverse_lazy('accounts:login')
    # tylko admin

    # sprawdzamy czy użytkownik ma uprawnienia
    permission_required = ('app1.add_brand', 'app1.add_category',
                           'app1.add_color', 'app1.add_size', 'app1.add_product')

    def get(self, request):
        count = {
            'brand': Brand.objects.all().count(),
            'category': Category.objects.all().count(),
            'color': Color.objects.all().count(),
            'product': Product.objects.all().count(),
            'size': Size.objects.all().count(),
        }
        # breakpoint()
        return render(request,
                      self.template_name,
                      context={
                          "count": count,
                      }
                      )
# ------------------------ Category ------------------------

class CategoryView(View):
    '''
    wyświetla listę dostępnych kategorii
    '''

    template_name = 'app1/category_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        categories = Category.objects.all().order_by('name')
        ctx = {
            'categories': categories,
        }
        return render(request, self.template_name, ctx)

class CategoryAddView(View):
    '''
    dodaj element do listy kategorii,
    sprawdza czy podana kategoria już istnieje
    '''

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
    '''
    wyświetl listę dostępnych rozmiarów
    '''

    template_name = 'app1/size_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        sizes = Size.objects.all()
        ctx = {
            'sizes': sizes,
        }
        return render(request, self.template_name, ctx)

class SizeAddView(View):
    '''
    dodaj element do listy rozmiarów
    sprawdza czy podany rozmiar już isteje
    '''

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
    '''
    wyświetla rozmiar o określonym size_id
    '''

    template_name = 'app1/size_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None

        size_id = kwargs['pk']

        # size = Size.objects.get(pk=size_id)
        #  404
        size = get_object_or_404(Size, pk=size_id)

        ctx = {
            'size': size,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------- Brand -------------------------

class BrandView(View):
    '''
    wyświetla listę dostępnych brandów
    '''
    template_name = 'app1/brand_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        brands = Brand.objects.all()
        ctx = {
            'brands': brands,
        }
        return render(request, self.template_name, ctx)

class BrandAddView(View):
    '''
    dodaje element do listy brandów
    sprawdza czy podany brand już istnieje
    '''

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
    '''
    wyświetla brand o określonym brand_id
    '''

    template_name = 'app1/brand_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None

        brand_id = kwargs['pk']

        # brand = Brand.objects.get(pk=brand_id)
        #  404
        brand = get_object_or_404(Brand, pk=brand_id)
        ctx = {
            'brand': brand,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------ Color ------------------------

class ColorView(View):
    '''
    wyświetla listę dostępnych kolorów
    '''

    template_name = 'app1/color_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        colors = Color.objects.all()
        ctx = {
            'colors': colors,
        }
        return render(request, self.template_name, ctx)

class ColorAddView(View):
    '''
    dodaje element do listy kolorów
    sprawdza czy podany kolor już istnieje
    '''

    template_name = 'app1/color_add.html'

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

        # breakpoint()
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
                return redirect("color")
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
    '''
    wyświetla kolor o określonym color_id
    '''

    template_name = 'app1/color_detail_view.html'

    def get(self, request, *args, **kwargs):
        message = None

        color_id = kwargs['pk']

        # color = Color.objects.get(pk=color_id)
        #  404
        color = get_object_or_404(Color, pk=color_id)

        ctx = {
            'color': color,
            'message': message
        }

        return render(request, self.template_name, ctx)

# ------------------------ Product ------------------------


class ProductView(View):
    '''
    wyświetla listę dostępnych towarów/produktów
    '''

    template_name = 'app1/product_view.html'

    def get(self, request, *args, **kwargs):
        # category = get_object_or_404(Student, pk=student_id)
        products = Product.objects.all()
        ctx = {
            'products': products,
        }
        return render(request, self.template_name, ctx)

class ProductAddView(View):
    '''
    dodaje element do listy produktów/towarów
    sprawdza czy podany produkt już istnieje
    '''
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
    '''
    wyświetla produkt/towar o określonym product_id
    '''

    template_name = 'app1/product_detail_view.html'


    def get(self, request, *args, **kwargs):
        message = None

        product_id = kwargs['pk']

        # product = Product.objects.get(pk=product_id)
        #  404
        product = get_object_or_404(Product, pk=product_id)
        # breakpoint()
        size = product.size.values()[0]['name']

        # breakpoint()
        categories = product.category.all()
        ctx = {
            'product': product,
            'categories': categories,
            'size': size,
            'message': message
        }

        return render(request, self.template_name, ctx)


# ------------------------ KlientProduct ------------------------
# class KlientProductView(LoginRequiredMixin, View):
class KlientProductView(View):
    '''
    dodaje element do listy dostępnych zestawów towarów/produktów
    '''

    template_name = 'app1/klient_product_list.html'

    def get(self, request, *args, **kwargs):
        is_logged = request.user.is_authenticated

        is_visible_dashboard = False


        if len(request.user.groups.all()) != 0:
            #  nie należy do żadnej
            NAME_GROUP = 'magazynierzy'
            # dla magazynierów
            if request.user.groups.get(name=NAME_GROUP).name == NAME_GROUP:
                is_visible_dashboard = True
        #     dla admina
        elif request.user.username == 'admin':
            is_visible_dashboard = True



        # breakpoint()
        products = Product.objects.all()
        sizes = Size.objects.all()
        categories = Category.objects.all()

        # podaj informacje o koszyku
        # jeśli klient nie zalogowany to nie pokazuj koszyka
        # ograniczenie dostępu - użytkownik nie zalogowany
        # login_url = reverse_lazy('accounts:login')
        # czy użytkownik jest zalogowany?

        # breakpoint()
        product_ile = 0

        if is_logged:
            koszyks = Koszyk.objects.all()

            for koszyk in koszyks:
                product_ile += koszyk.ile


        else:
            koszyks = None
        # breakpoint()

        lista_prod = []
        element = None
        # breakpoint()
        for prod in products:
            element = {
                'pk': prod.pk,
                'name': prod.name,
                'price': prod.price,
                'size': prod.size.all(),
                'color': prod.color,
                'brand': prod.brand,
            }
            lista_prod.append(element)

        # breakpoint()
        # Product.objects.get(pk=1).size.values()
        # Product.objects.get(pk=1).color.values()

        ctx = {
            'product': products,
            'sizes': sizes,
            'categories': categories,
            'lista_prods': lista_prod,
            'product_ile': product_ile,
            'is_logged': is_logged,
            'is_visible_dashboard': is_visible_dashboard


        }
        # form = KlientProductAddForm()
        # # breakpoint()
        # ctx = {
        #     'form': form,
        # }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        ctx = {
            # 'form': form,
            # 'message': message,
            }
        return render(request, self.template_name, ctx)

class KlientProductKoszykView(LoginRequiredMixin, View):
    '''
    wyświetla element z listy dostępnych zestawów towarów/produktów
    o określonym product_id
    '''

    template_name = 'app1/klient_product_koszyk.html'

    # ograniczenie dostępu - użytkownik nie zalogowany
    login_url = reverse_lazy('accounts:login')

    success_url = 'klient-product'

    def get(self, request, *args, **kwargs):
        product_id = kwargs['pk']

        product = get_object_or_404(Product, pk=product_id)
        # breakpoint()
        size = product.size.values()[0]['name']
        color = product.color

        ctx = {
            'product': product,
            'size': size,
            'color': color,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        # breakpoint()

        # len_koszyk = len(Koszyk.objects.all())
        message = ''
        try:

            koszyk = Koszyk.objects.get(product=product_id)
        except Koszyk.DoesNotExist:
            koszyk = None


            # koszyk = get_object_or_404(Koszyk, product = product_id)

            # breakpoint()
            # sprawdzaj czy jest już towar o takim id
        if koszyk != None:
            # koszyk = Koszyk()
            # koszyk.product = product_id
            koszyk.ile += 1
            koszyk.save()

        else:
            koszyk = Koszyk()
            # koszyk.add(product = product_id, ile = 1)
            koszyk.product = Product.objects.get(pk=product_id)
            koszyk.ile = 1
            koszyk.save()

        koszyk = Koszyk.objects.all()
        # breakpoint()
        ctx = {
            # 'form': form,
            'message': message,
            'koszyk': koszyk,
            }
        return render(request, self.template_name, ctx)

class KlientKoszykView(View):
    '''
    wyświetl zawartość koszyka
    '''

    template_name = 'app1/klient_product_koszyk_detail.html'


    def get(self, request, *args, **kwargs):
        koszyks = Koszyk.objects.all()
        # product = Product.objects.all()

        elements = []
        # breakpoint()
        product_suma = 0
        koszyk_id = 1
        for koszyk in koszyks:
            elements.append(
                {'id': koszyk_id,
                 'name': koszyk.product.name,
                 'brand': koszyk.product.brand.name,
                 'color': koszyk.product.color.name,
                 'size': koszyk.product.size.values('name')[0]['name'],
                 'category': koszyk.product.category.values('name')[0]['name'],
                 'price': koszyk.product.price,
                 'ile': koszyk.ile
                 }
            )
            koszyk_id += 1
            product_suma += koszyk.product.price * koszyk.ile

        message = None

        # breakpoint()
        ctx = {
            'message': message,
            'elements': elements,
            'product_suma': product_suma,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        koszyk = Koszyk.objects.all()
        ctx = {
            # 'form': form,
            'message': message,
            'koszyk': koszyk,
            }
        return render(request, self.template_name, ctx)