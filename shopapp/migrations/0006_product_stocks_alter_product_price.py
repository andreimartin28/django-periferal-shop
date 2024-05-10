# Generated by Django 4.2.6 on 2023-10-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stocks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]
