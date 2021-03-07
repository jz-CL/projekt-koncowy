from random import choice, randint
from sys import stdout
# from faker import Factory


from app1.models import Size, Category, Color, Brand

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




    Category.objects.create(name='Sukienki') #
    Category.objects.create(name='Koszulki i topy') #
    # Category.objects.create(name='Bluzki i koszule')
    # Category.objects.create(name='Swetry i kardigany')
    Category.objects.create(name='Bluzy') ##
    # Category.objects.create(name='Kurtki i marynarki')
    # Category.objects.create(name='Płaszcze')
    # Category.objects.create(name='Jeansy')
    Category.objects.create(name='Spodnie')
    # Category.objects.create(name='Kombinezony i ogrodniczki')
    Category.objects.create(name='Spódnice')
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




