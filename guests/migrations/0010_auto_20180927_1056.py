# Generated by Django 2.1 on 2018-09-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_rsvp_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='message',
            field=models.TextField(blank=True, default=''),
        ),
    ]
