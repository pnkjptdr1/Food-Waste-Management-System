# Generated by Django 3.2.5 on 2023-08-22 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DonateRecieve', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='student',
            new_name='donor',
        ),
    ]