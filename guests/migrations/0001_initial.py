# Generated by Django 2.1 on 2018-09-22 19:40

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('percentile', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('likelihood', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('family', models.PositiveSmallIntegerField(choices=[(1, 'Bride'), (2, 'Groom'), (3, 'Friend')], default=3)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('ar', 'Arabic')], default='en', max_length=2)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('kuwait_invite', models.BooleanField(default=False)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('administrative_area', models.CharField(blank=True, max_length=60, verbose_name='state')),
                ('sub_administrative_area', models.CharField(blank=True, max_length=60, verbose_name='county')),
                ('locality', models.CharField(blank=True, max_length=60, verbose_name='city')),
                ('dependent_locality', models.CharField(blank=True, max_length=60, verbose_name='neighborhood')),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('thoroughfare', models.CharField(blank=True, max_length=60, verbose_name='street address')),
                ('premise', models.CharField(blank=True, max_length=60, verbose_name='apartment/box')),
                ('sub_premise', models.CharField(blank=True, max_length=60, verbose_name='room')),
                ('notes', models.TextField(blank=True)),
                ('lead_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner', to='guests.Guest')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='guests.Guest')),
            ],
        ),
    ]
