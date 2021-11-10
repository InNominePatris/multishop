# Generated by Django 2.2 on 2021-11-10 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('dealer', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('deliver_address', models.CharField(max_length=25, verbose_name='Deliver address')),
                ('observations', models.TextField(max_length=200, verbose_name='Observations')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Customer')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer', verbose_name='Dealer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]