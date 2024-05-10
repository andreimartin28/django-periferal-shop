# Generated by Django 4.2.6 on 2023-10-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0017_alter_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('RON', 'RON'), ('EURO', 'EURO')], max_length=50),
        ),
    ]
