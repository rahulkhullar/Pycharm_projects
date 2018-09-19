# Generated by Django 2.2.dev20180608160017 on 2018-06-14 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.CharField(max_length=200)),
                ('street2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('primary_phone', models.CharField(max_length=200)),
                ('secondary_phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
                ('primary_phone', models.CharField(max_length=200)),
                ('secondary_phone', models.CharField(max_length=200)),
                ('billing_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('address_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Address')),
                ('customer_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Orderline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=200)),
                ('unit_price', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateTimeField()),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=400)),
                ('dest_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Address')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Item')),
                ('orderline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Orderline')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('address_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Address')),
            ],
        ),
        migrations.AddField(
            model_name='shipment',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Supplier'),
        ),
        migrations.AddField(
            model_name='itemsupply',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.Supplier'),
        ),
    ]