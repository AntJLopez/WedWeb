# Generated by Django 2.1 on 2018-08-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0015_auto_20180805_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('ar', 'Arabic')], default='en', max_length=2),
        ),
    ]