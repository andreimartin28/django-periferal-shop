# Generated by Django 4.2.6 on 2023-10-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0020_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
