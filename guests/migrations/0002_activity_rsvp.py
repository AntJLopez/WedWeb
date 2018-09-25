# Generated by Django 2.1 on 2018-09-25 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attending', models.BooleanField()),
                ('attending_kuwait', models.BooleanField(default=False)),
                ('nights_onsite', models.PositiveSmallIntegerField(default=0)),
                ('activities', models.ManyToManyField(related_name='participants', to='guests.Activity')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guests.Guest')),
            ],
        ),
    ]
