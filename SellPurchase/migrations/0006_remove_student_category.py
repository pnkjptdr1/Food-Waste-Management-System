# Generated by Django 3.2.5 on 2023-08-22 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SellPurchase', '0005_auto_20230822_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='category',
        ),
    ]