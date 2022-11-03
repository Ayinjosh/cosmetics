# Generated by Django 4.1.1 on 2022-11-01 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_shopcart_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopcart',
            options={'managed': True, 'verbose_name': 'Shopcart', 'verbose_name_plural': 'Shopcarts'},
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cart_no', models.CharField(max_length=50)),
                ('pay_code', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('New', 'New'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='NEW', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('admin_note', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
                'managed': True,
            },
        ),
    ]
