# Generated by Django 4.2.6 on 2024-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0045_alter_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
