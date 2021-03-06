from django.contrib import messages
from django.shortcuts import render, redirect

from django.views import View
from django.core.exceptions import ValidationError

# Create your views here.
from app1.forms import CategoryAddForm, SizeAddForm, ProductAddForm
from app1.models import Category, Size, Product


# TODO uzupełnić Product

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
            # breakpoint()
            category_len = len(Category.objects.filter(name=name))
            if category_len == 0:
                category = Category()
                category.name = name
                category.save()

                messages.success(request, 'Dodano nową kategorię.')

                # -> przekieruj na stronę category
                return redirect("category")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                message = 'Ta kategoria już jest!'
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
            # breakpoint()
            size_len = len(Size.objects.filter(name=name))
            if size_len == 0:
                size = Size()
                size.name = name
                size.save()

                messages.success(request, 'Dodano nowy rozmiar.')

                # -> przekieruj na stronę size
                return redirect("size")
            else:
                # raise ValidationError('Ta kategoria już jest!')  # rzuć wyjątek
                # breakpoint()
                message = 'Ten rozmiar już jest!'
        #  jeśli nie przeszła walidacja to renderuj na stronie...
        ctx = {
            'form': form,
            'message': message,
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

            # breakpoint()
            product_len = len(Product.objects.filter(name=name))
            if product_len == 0:
                product = Product()

                product.name = name
                product.description = description
                product.price = price
                product.current_quantity = current_quantity
                product.size = size
                # product.category = category


                product.save()
                # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
                product.category.add(category)

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
        # breakpoint()
        product = Product.objects.get(pk=product_id)
        categories = product.category.all()
        # breakpoint()
        ctx = {
            # 'form': form,
            'product': product,
            'categories': categories,
            'message': message
        }

        return render(request, self.template_name, ctx)