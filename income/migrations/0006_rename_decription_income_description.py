# Generated by Django 4.1.5 on 2024-09-27 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0005_alter_income_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='decription',
            new_name='description',
        ),
    ]