from django.contrib import admin
from .models import Address, Customer, Item, Order, Orderline, Supplier, ItemSupply, Shipment, ItemCategory


# Register your models here.

admin.site.register(Address)
#admin.site.register(Customer)
admin.site.register(Item)
#admin.site.register(Order)
admin.site.register(Orderline)
admin.site.register(Supplier)
admin.site.register(ItemSupply)
admin.site.register(Shipment)
admin.site.register(ItemCategory)


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1 

class CustomerAddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer Information',{'fields': ['first_name', 'last_name', 'email_address']}),
       # ('Date information', {'fields': ['last_name'], 'classes': ['collapse']}),
    ]
    inlines = [AddressInline]

admin.site.register(Customer, CustomerAddressAdmin)

class OrderlineInline(admin.StackedInline):
    model = Orderline
#    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer Information',{'fields': ['customer_id']}),
       # ('Date information', {'fields': ['last_name'], 'classes': ['collapse']}),
    ]
    inlines = [OrderlineInline]
    list_display = (Order, 'customer_id', 'order_date') 
admin.site.register(Order, OrderAdmin)


