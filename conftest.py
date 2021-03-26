import pytest

# from django.test import Client
from app1.models import Category, Size, Color, Brand, Product
# from django.core.management import call_command


# @pytest.fixture
# def client():
#     return Client()

# ------------------ category -------------------------

@pytest.fixture
def addCategory():
    Category.objects.create(name='Sukienki', kod='C')  #
    Category.objects.create(name='Koszulki i topy', kod='D')

# ------------------ size -------------------------

@pytest.fixture
def addSize():
    Size.objects.create(name='34', kod='FE')
    Size.objects.create(name='35', kod='GE')
    Size.objects.create(name='36', kod='HE')

# ------------------ color -------------------------

@pytest.fixture
def addColor():
    Color.objects.create(name='czarny', kod='Q')
    Color.objects.create(name='biały', kod='A')
    Color.objects.create(name='czerwony', kod='K')

# ------------------ brand -------------------------

@pytest.fixture
def addBrand():
    Brand.objects.create(name='Guess', kod='GU')
    Brand.objects.create(name='Dorothy Perkins', kod='DP')


# ------------------ product -------------------------

@pytest.fixture
def addProduct(addBrand, addCategory, addColor, addSize):
    #  1
    brand = Brand.objects.get(name='Dorothy Perkins')
    category = Category.objects.get(name='Sukienki')
    color = Color.objects.get(name='czerwony')
    size = Size.objects.get(name='36')

    product = Product.objects.create(name='Sukienka koktajlowa',
                                     description='''
    Materiał: 97% poliester, 3% elastan
    Wskazówki pielęgnacyjne: Pranie w pralce w 30°C
    Długość: Średnia
    Długość rękawa: Długi rękaw
    ''',
                                     price=190,
                                     current_quantity=5,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

    # 2

    brand = Brand.objects.get(name='Dorothy Perkins')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='36')

    product = Product.objects.create(name='Bluzka',
                                     description='''
    Materiał: 100% poliester
    Wskazówki pielęgnacyjne: Pranie w pralce w 30°C
    Wzór: Kolor jednolity
    ''',
                                     price=109,
                                     current_quantity=10,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

#  -----------------------------------------------

@pytest.fixture
def addProductView(addBrand, addCategory, addColor, addSize, addProduct):


    brand = Brand.objects.get(name='Dorothy Perkins')
    category = Category.objects.get(name='Sukienki')
    color = Color.objects.get(name='czerwony')
    size = Size.objects.get(name='36')

    return (brand, category, color, size, addProduct)