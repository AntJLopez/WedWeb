# Generated by Django 2.1 on 2018-09-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0023_guest_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='username',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]