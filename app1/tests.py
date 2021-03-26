# from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client
from app1.models import Category, Size, Color, Brand, Product

# Create your tests here.
# sprawdzenie status code200
# sprawdzenie ile jest rekordow w bazie danych

# ------------------ category -------------------------
#  pytest app1/tests.py::test_category_view -v

@pytest.mark.django_db
def test_category_view(addCategory, client):

    response = client.get('/category/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    # 'categories': categories, -> z kontextu
    assert len(response.context['categories']) == 2

#  pytest app1/tests.py::test_category_add_view -v

@pytest.mark.django_db
def test_category_add_view(client):
    # response = client.get('/category_add/')
    # assert response.status_code == 200
    response = client.post('/category_add/',
                           {'name':'kategoria 1',
                            'kod':'KA'}
                           )
    # assert Category.objects.filter(name="kategoria 1").count() > 0
    assert Category.objects.filter(name="kategoria 1")
    assert Category.objects.filter(kod="KA")
    assert response.status_code == 302

# ------------------ size -------------------------
# pytest app1/tests.py::test_size_view -v

@pytest.mark.django_db
def test_size_view(addSize, client):

    response = client.get('/size/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    assert len(response.context['sizes']) == 3

# pytest app1/tests.py::test_size_add_view -v

@pytest.mark.django_db
def test_size_add_view(client):
    response = client.post('/size_add/',
                           {'name':'SIZE 1',
                            'kod':'S1'}
                           )

    assert Size.objects.filter(name="SIZE 1")
    assert Size.objects.filter(kod="S1")
    assert response.status_code == 302

# ------------------ color -------------------------
# pytest app1/tests.py::test_color_view -v

@pytest.mark.django_db
def test_color_view(addColor, client):

    response = client.get('/color/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    assert len(response.context['colors']) == 3

# pytest app1/tests.py::test_color_add_view -v

@pytest.mark.django_db
def test_color_add_view(client):
    response = client.post('/color_add/',
                           {'name':'kolor',
                            'kod':'K'}
                           )

    assert Color.objects.filter(name="kolor")
    assert Color.objects.filter(kod="K")
    assert response.status_code == 302

# ------------------ brand -------------------------
# pytest app1/tests.py::test_brand_view -v

@pytest.mark.django_db
def test_brand_view(addBrand, client):

    response = client.get('/brand/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    assert len(response.context['brands']) == 2

# pytest app1/tests.py::test_brand_add_view -v

@pytest.mark.django_db
def test_brand_add_view(client):
    response = client.post('/brand_add/',
                           {'name':'Pepa',
                            'kod':'PE'}
                           )

    assert Brand.objects.filter(name="Pepa")
    assert Brand.objects.filter(kod="PE")
    assert response.status_code == 302

# ------------------ product -------------------------
# pytest app1/tests.py::test_product_view -v

@pytest.mark.django_db
def test_product_view(addProduct, client):

    response = client.get('/product/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    assert len(response.context['products']) == 2

# pytest app1/tests.py::test_product_add_view -v

@pytest.mark.django_db
def test_product_add_view(addProductView, client):
    (brand, category, color, size, product) = addProductView


    response = client.post('/product_add/',
                           {'name':'PeP',
                            'description':'cośTam',
                            'price': 100,
                            'current_quantity': 25,
                            'category': category.pk,
                            'size': size.pk,
                            'brand': brand.pk,
                            'identifier_exists': brand.kod + category.kod + size.kod,
                            'color': color.pk}
                           )

    # assert response.context['form'].errors
    assert Product.objects.filter(name="PeP")
    assert response.status_code == 302

# def test_login(client, funkcjatworzacaUser):
#     response = client.login(unsername='username', password='password')
#     code == 200
#
#     response = client.login(unsername='username', password='zle haslo')
#     code == 401