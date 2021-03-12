from random import choice, randint
from sys import stdout
# from faker import Factory


from app1.models import Size, Category, Color, Brand, Product

# def create_name():
#     fake = Factory.create("pl_PL")
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     return first_name, last_name

def create_color():
    Color.objects.create(name='czarny', kod='Q')
    Color.objects.create(name='biały', kod='A')
    Color.objects.create(name='zielony', kod='M')
    Color.objects.create(name='beżowy', kod='H')
    Color.objects.create(name='czerwony', kod='K')

def create_brand():
    Brand.objects.create(name='Dorothy Perkins', kod='DP')
    Brand.objects.create(name='JDY', kod='JY')
    Brand.objects.create(name='Even&Odd', kod='EV')
    Brand.objects.create(name='GAP', kod='GP')
    Brand.objects.create(name='Anna Field', kod='AN')
    Brand.objects.create(name='Tommy Hilfiger', kod='TO')
    Brand.objects.create(name="Marc O'Polo", kod='MA')
    Brand.objects.create(name='Guess', kod='GU')
    Brand.objects.create(name='Monki', kod='MO')
    Brand.objects.create(name='PULL&BEAR', kod='PU')



def create_size():
    # Size.objects.create(name='23')
    # Size.objects.create(name='24')
    # Size.objects.create(name='25')
    # Size.objects.create(name='26')
    # Size.objects.create(name='27')
    # Size.objects.create(name='28')
    # Size.objects.create(name='29')
    # Size.objects.create(name='30')
    # Size.objects.create(name='31')
    # Size.objects.create(name='32')
    # Size.objects.create(name='33')
    Size.objects.create(name='34', kod='FE')
    Size.objects.create(name='35', kod='GE')
    Size.objects.create(name='36', kod='HE')
    Size.objects.create(name='37', kod='JE')
    Size.objects.create(name='38', kod='KE')
    Size.objects.create(name='39', kod='LE')
    Size.objects.create(name='40', kod='AR')
    Size.objects.create(name='41', kod='SR')
    Size.objects.create(name='42', kod='DR')
    Size.objects.create(name='44', kod='FR')
    Size.objects.create(name='46', kod='GR')
    Size.objects.create(name='48', kod='HR')
    Size.objects.create(name='50', kod='FT')
    Size.objects.create(name='52', kod='GT')
    Size.objects.create(name='54', kod='HT')
    Size.objects.create(name='56', kod='JT')
    # Size.objects.create(name='70B')
    # Size.objects.create(name='70C')
    # Size.objects.create(name='70D')
    # Size.objects.create(name='75B')
    # Size.objects.create(name='75C')
    # Size.objects.create(name='75D')
    # Size.objects.create(name='75E')
    # Size.objects.create(name='80B')
    # Size.objects.create(name='80C')
    # Size.objects.create(name='80D')
    # Size.objects.create(name='80E')
    # Size.objects.create(name='85B')
    # Size.objects.create(name='85C')
    # Size.objects.create(name='85D')
    # Size.objects.create(name='85E')
    # Size.objects.create(name='XXS', kod='SY')
    # Size.objects.create(name='XS', kod='SY')
    # Size.objects.create(name='S', kod='SY')
    # Size.objects.create(name='M', kod='SY')
    # Size.objects.create(name='L', kod='SY')
    # Size.objects.create(name='XL', kod='SY')
    # Size.objects.create(name='XXL', kod='SY')

def create_category():
    # Category.objects.create(name='Kobiety')
    # Category.objects.create(name='Mężczyźni')
    # Category.objects.create(name='Dzieci')




    Category.objects.create(name='Sukienki', kod='C') #
    Category.objects.create(name='Koszulki i topy', kod='D') #
    # Category.objects.create(name='Bluzki i koszule')
    # Category.objects.create(name='Swetry i kardigany')
    Category.objects.create(name='Bluzy', kod='E') ##
    # Category.objects.create(name='Kurtki i marynarki')
    # Category.objects.create(name='Płaszcze')
    # Category.objects.create(name='Jeansy')
    Category.objects.create(name='Spodnie', kod='A')
    # Category.objects.create(name='Kombinezony i ogrodniczki')
    Category.objects.create(name='Spódnice', kod='B')
    # Category.objects.create(name='Bielizna i piżamy')
    # Category.objects.create(name='Skarpety i rajstopy')
    # Category.objects.create(name='Odzież sportowa')
    # Category.objects.create(name='Moda plażowa')

    # Category.objects.create(name='Koszulki')
    # Category.objects.create(name='Koszule')
    # Category.objects.create(name='Bluzy i swetry')
    # Category.objects.create(name='Kurtki i marynarki')
    # Category.objects.create(name='Płaszcze')
    # Category.objects.create(name='Jeansy')
    # Category.objects.create(name='Spodnie')
    # Category.objects.create(name='Garnitury i akcesoria')
    # Category.objects.create(name='Bielizna i piżamy')
    # Category.objects.create(name='Skarpety')
    # Category.objects.create(name='Odzież sportowa')
    # Category.objects.create(name='Moda plażowa')
    #
    # Category.objects.create(name='Koszulki i T-shirty')
    # Category.objects.create(name='Kurtki i płaszcze')
    # Category.objects.create(name='Garnitury')
    # Category.objects.create(name='Sukienki')
    # Category.objects.create(name='Swetry i bluzy')
    # Category.objects.create(name='Spodnie i jeansy')
    # Category.objects.create(name='Kombinezony')
    # Category.objects.create(name='Spódnice')
    # Category.objects.create(name='Odzież sportowa')
    # Category.objects.create(name='Bielizna i piżamy')
    # Category.objects.create(name='Skarpety i rajstopy')
    # Category.objects.create(name='Moda plażowa')
    # Category.objects.create(name='Prezenty z okazji narodzin')



def create_product():
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
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 2

    brand = Brand.objects.get(name='Dorothy Perkins')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='beżowy')
    size = Size.objects.get(name='36')


    product = Product.objects.create(name='Bluzka',
                           description='''
Materiał: 100% poliester
Wskazówki pielęgnacyjne: Pranie w pralce w 30°C
Wzór: Kolor jednolity
''',
                           price=109,
                           current_quantity=10,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 3

    brand = Brand.objects.get(name='Dorothy Perkins')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='zielony')
    size = Size.objects.get(name='34')


    product = Product.objects.create(name='Bluzka',
                           description='''
Materiał: 100% poliester
Wskazówki pielęgnacyjne: Pranie w pralce w 30°C
Długość rękawa: Krótki rękaw
''',
                           price=130,
                           current_quantity=20,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 4

    brand = Brand.objects.get(name='JDY')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='42')


    product = Product.objects.create(name='JDYBLOND',
                           description='''
Materiał: 100% poliester
Struktura/rodzaj materiału: Koronka
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, materiał może maksymalnie zbiec się o 5%, pranie delikatne
Długość: Standardowa
Długość rękawa: Bardzo krótki rękawek
''',
                           price=59,
                           current_quantity=15,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 5

    brand = Brand.objects.get(name='JDY')
    category = Category.objects.get(name='Sukienki')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='44')


    product = Product.objects.create(name='JDYBLOND',
                           description='''
Materiał: 100% poliester
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie delikatne, nie wybielać
''',
                           price=169.99,
                           current_quantity=15,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 6

    brand = Brand.objects.get(name='JDY')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='42')


    product = Product.objects.create(name='JDYCARMEN',
                           description='''
Materiał: 100% poliester
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie delikatne, nie wybielać
''',
                           price=99,
                           current_quantity=15,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 7

    brand = Brand.objects.get(name='Even&Odd')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='biały')
    size = Size.objects.get(name='38')


    product = Product.objects.create(name='Top',
                           description='''
Materiał: 100% poliester
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie delikatne, nie wybielać
''',
                           price=79,
                           current_quantity=12,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 8

    brand = Brand.objects.get(name='Even&Odd')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='biały')
    size = Size.objects.get(name='38')


    product = Product.objects.create(name='Bluzka z długim rękawem',
                           description='''
Materiał: 95% wiskoza, 5% elastan
Górna część: 95% poliester, 5% elastan
Struktura/rodzaj materiału: Dżersej, tiul
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Długość: Standardowa
Długość rękawa: Długi rękaw
''',
                           price=79,
                           current_quantity=16,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 9

    brand = Brand.objects.get(name='Even&Odd')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='40')


    product = Product.objects.create(name='Bluzka z długim rękawem',
                           description='''
Materiał: 95% wiskoza, 5% elastan
Górna część: 95% poliester, 5% elastan
Struktura/rodzaj materiału: Dżersej, tiul
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Długość: Standardowa
Długość rękawa: Długi rękaw
''',
                           price=79,
                           current_quantity=16,
                           brand_id = brand.id,
                           color_id = color.id,
                           identifier_exists = brand.kod + category.kod + size.kod + color.kod
                           # brand.kod + category.kod +   + color.kod
                           )

    product.category.add(category)
    product.size.add(size)

    # 10

    brand = Brand.objects.get(name='Even&Odd')
    category = Category.objects.get(name='Spodnie')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='40')

    product = Product.objects.create(name='Spodnie treningowe',
                                     description='''
Materiał: 60% bawełna, 40% poliester
Struktura/rodzaj materiału: Dres
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Wzór: Kolor jednolity
Szczegóły: Elastyczna talia
    ''',
                                     price=74,
                                     current_quantity=16,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

    # 11

    brand = Brand.objects.get(name="Marc O'Polo")
    category = Category.objects.get(name='Spodnie')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='44')

    product = Product.objects.create(name='MARIKO SKIRT',
                                     description='''
Materiał: 72% wiskoza, 24% nylon, 4% elastan
Struktura/rodzaj materiału: Dżersej
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Wzór: Kolor jednolity
Szczegóły: Elastyczna talia
        ''',
                                     price=249,
                                     current_quantity=11,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

    # 12

    brand = Brand.objects.get(name='Tommy Hilfiger')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='44')

    product = Product.objects.create(name='Koszulka polo',
                                     description='''
Materiał: 72% wiskoza, 24% nylon, 4% elastan
Struktura/rodzaj materiału: Dżersej
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Wzór: Kolor jednolity
Szczegóły: Elastyczna talia
Długość: Do kolan
        ''',
                                     price=269,
                                     current_quantity=16,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

    # 13

    brand = Brand.objects.get(name='Guess')
    category = Category.objects.get(name='Koszulki i topy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='40')

    product = Product.objects.create(name='KUMIKO',
                                     description='''
Materiał: 72% wiskoza, 24% nylon, 4% elastan
Struktura/rodzaj materiału: Dżersej
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej, pranie w pralce w 30°C, pranie delikatne
Wzór: Kolor jednolity
Szczegóły: Elastyczna talia
Długość: Do kolan
        ''',
                                     price=169,
                                     current_quantity=18,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)

    # 14

    brand = Brand.objects.get(name='Monki')
    category = Category.objects.get(name='Bluzy')
    color = Color.objects.get(name='zielony')
    size = Size.objects.get(name='38')

    product = Product.objects.create(name='MISA',
                                     description='''
Materiał: 60% bawełna, 40% poliester
Struktura/rodzaj materiału: Dres
Wskazówki pielęgnacyjne: Pranie w pralce w 40°C, nie suszyć w suszarce bębnowej
Rodzaj dekoltu: Okrągły
Wzór: Kolor jednolity
Szczegóły: Elastyczna talia
        ''',
                                     price=99,
                                     current_quantity=18,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)


    # 15

    brand = Brand.objects.get(name='PULL&BEAR')
    category = Category.objects.get(name='Bluzy')
    color = Color.objects.get(name='czarny')
    size = Size.objects.get(name='38')

    product = Product.objects.create(name='Bluzka',
                                     description='''
Materiał: 98% bawełna, 2% elastan
Wskazówki pielęgnacyjne: Nie suszyć w suszarce bębnowej
Długość rękawa: Długi rękaw
        ''',
                                     price=49.99,
                                     current_quantity=18,
                                     brand_id=brand.id,
                                     color_id=color.id,
                                     identifier_exists=brand.kod + category.kod + size.kod + color.kod
                                     # brand.kod + category.kod +   + color.kod
                                     )

    product.category.add(category)
    product.size.add(size)