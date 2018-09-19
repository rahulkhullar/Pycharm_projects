from django.db import models
from django.utils import timezone
from .constants import state_choices
import datetime

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email_address = models.EmailField(max_length=200, null=True, blank=True)
#    primary_phone = models.CharField(max_length=200, null=True, blank=True)
#    secondary_phone = models.CharField(max_length=200, null=True, blank=True)
    #address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Address(models.Model):
    street1 = models.CharField(max_length=200, null=True, blank=True)
    street2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True, choices = state_choices)
    country = models.CharField(max_length=200, null=True, blank=True, default= 'US', editable=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    primary_phone = models.CharField(max_length=200, null=True, blank=True)
    secondary_phone = models.CharField(max_length=200, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

class ItemCategory(models.Model):
    category_name = models.CharField(max_length=200, default = 'Category')
    category_description = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=200, default='Item name')
    description = models.CharField(max_length=300, null=True, blank=True)
    category_id = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, default='Unbranded')
    image_url = models.ImageField(upload_to='item_images/', null=True, blank=True)
    def __str__(self):
        return self.item_name + "/" + self.description


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return "ORDER"+self.id.__str__()


class Orderline(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status_choices = ( ('CREATED','CREATED'), ('CONFIRMED', 'CONFIRMED'), ('SHIPPED', 'SHIPPED'), ('DELIVERED', 'DELIVERED'))
    status = models.CharField(max_length=200, choices = status_choices, default = 'CREATED'  )
    unit_price = models.IntegerField(default=0)
#    shipping_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    street1 = models.CharField(max_length=200, null=True, blank=True)
    street2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    primary_phone = models.CharField(max_length=200, null=True, blank=True)
    secondary_phone = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.supplier_name + ", " + self.city + ", " + self.country

class ItemSupply(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=200)

class Shipment(models.Model):
    shipment_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    orderline_id = models.ForeignKey(Orderline, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    dest_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    remarks = models.CharField(max_length=400, null=True, blank=True)

