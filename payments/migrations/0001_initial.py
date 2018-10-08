# Generated by Django 2.1 on 2018-09-25 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '0002_activity_rsvp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guests.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stripe_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='payments.PaymentCategory')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.PaymentCategory'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Payer'),
        ),
    ]