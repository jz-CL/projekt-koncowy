# Generated by Django 3.0.6 on 2021-03-18 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210312_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koszyk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ile', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='koszyks', to='app1.Product')),
            ],
        ),
    ]
