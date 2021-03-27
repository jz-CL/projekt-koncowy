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

# pytest app1/tests.py::test_size_detail_view -v --pdb

@pytest.mark.django_db
def test_size_detail_view(addSize, client):
    response = client.get('/size_detail/1')

    # url = reverse(
    #     'size_detail', kwargs={'pk': 1}
    # )
    #
    # response = client.get(url)

    assert response.context['size'].name == '34'
    assert response.status_code == 200

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

# pytest app1/tests.py::test_color_detail_view -vvv --pdb

@pytest.mark.django_db
def test_color_detail_view(addColor, client):
    response = client.get('/color_detail/1')

    # url = reverse(
    #     'color_detail', kwargs={'pk': 1}
    # )
    #
    # response = client.get(url)

    assert response.context['color'].name == 'czarny'
    assert response.status_code == 200
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

# pytest app1/tests.py::test_brand_detail_view -vvv --pdb

@pytest.mark.django_db
def test_brand_detail_view(addBrand, client):
    response = client.get('/brand_detail/1')

    # url = reverse(
    #     'brand_detail', kwargs={'pk': 1}
    # )
    #
    # response = client.get(url)

    assert response.context['brand'].name == 'Guess'
    assert response.status_code == 200

# ------------------ product -------------------------
# pytest app1/tests.py::test_product_view -v

@pytest.mark.django_db
def test_product_view(addProduct, client):

    response = client.get('/product/')
    assert response.status_code == 200

    #  z widoku z funkcji get
    assert len(response.context['products']) == 2

# pytest app1/tests.py::test_product_usr_view -vvv --pdb

@pytest.mark.django_db
def test_product_usr_view(addProduct, user, client):

    client.force_login(user)
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

# pytest app1/tests.py::test_product_add_usr_view -vvv --pdb

@pytest.mark.django_db
def test_product_add_usr_view(addProductView, user, client):
    (brand, category, color, size, product) = addProductView

    client.force_login(user)

    response = client.post('/product_add/',
                           {'name': 'PeP',
                            'description': 'cośTam',
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

# pytest app1/tests.py::test_product_detail_view -vvv --pdb

@pytest.mark.django_db
def test_product_detail_view(addProduct, client):
    response = client.get('/product_detail/1')

    # url = reverse(
    #     'product_detail', kwargs={'pk': 1}
    # )
    #
    # response = client.get(url)

    assert response.context['product'].name == 'Sukienka koktajlowa'
    assert response.status_code == 200


# pytest app1/tests.py::test_KlientProduct_view -vvv --pdb

@pytest.mark.django_db
def test_KlientProduct_view(client):
    response = client.get('')
    assert response.status_code == 200

# pytest app1/tests.py::test_KlientProduct_view -vvv --pdb

@pytest.mark.django_db
def test_KlientProduct_view(user, client):
    response = client.get('')
    assert response.status_code == 200

# pytest app1/tests.py::test_KlientKoszykAdd_view -vvv --pdb
@pytest.mark.django_db
def test_KlientKoszykAdd_view(client):
    response = client.get('/dodaj_do_koszyka/2')
    assert response.status_code == 302

# pytest app1/tests.py::test_KlientKoszykDelete_view -vvv --pdb
@pytest.mark.django_db
def test_KlientKoszykDelete_view(user, client):
    client.force_login(user)
    response = client.get('/koszyk_delete/')
    assert response.status_code == 302

# def test_login(client, funkcjatworzacaUser):
#     response = client.login(unsername='username', password='password')
#     code == 200
#
#     response = client.login(unsername='username', password='zle haslo')
#     code == 401