from django.shortcuts import render, render_to_response, redirect
from django.template import loader

from .models import Item, Customer, Address, Order, Orderline


# Create your views here.
def index (request):
    return render_to_response('oms/index.html')

#def shop (request):
#    return render_to_response('oms/shop.html')

def shop(request):
    item_list = Item.objects.order_by('-category_id')
#    template = loader.get_template('oms/shop.html')
    context = {
        'item_list': item_list,
    }
    return render(request, 'oms/shop.html', context)

def addcust(request, item_id):
#    item_list = Item.objects.order_by('-category_id')
#    template = loader.get_template('oms/shop.html')
    context = {
        'item_id': item_id,
    }
    return render(request, 'oms/addcust.html', context)

def savecust(request, item_id):
#def savecust(request, item_id):
#    item_list = Item.objects.order_by('-category_id')
#    template = loader.get_template('oms/shop.html')

    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email_address = request.POST["email_address"]
    street1 = request.POST["street1"]
    street2 = request.POST["street2"]
    city = request.POST["city"]
    state = request.POST["state"]
    country = request.POST["country"]
    zip_code = request.POST["zip_code"]
    primary_phone = request.POST["primary_phone"]
    secondary_phone = request.POST["secondary_phone"]

    customer = Customer(first_name= first_name,last_name= last_name,email_address= email_address)
    print(customer)
    customer.save()

    address = Address(customer_id=customer, street1=street1, street2=street2, city=city, state=state,
                  country=country, zip_code=zip_code, primary_phone=primary_phone,
                  secondary_phone=secondary_phone)

    address.save()
    context = {
        'item_id': item_id,
        'customer_id': customer.id
    }
    #return render(request, 'oms/context/savecust.html', context)
    return render(request, 'oms/savecust.html', context)

def order(request):
    customer_id = request.POST["customer_id"]
    item = Item.objects.get(pk=request.POST["item_id"])

    order = Order(customer_id=Customer.objects.get(pk=customer_id))
    order.save()

    orderline = Orderline(order_id= order, item_id =item, status = 'CREATED',
                          unit_price=item.price, quantity=1)
    orderline.save()

    return render(request,'oms/order.html')
