from django.shortcuts import render
from django.http import HttpResponse
from cart.models import Products , Contact , Order , OrderUpdate
import json


# Create your views here.
def home(request): 
    products = Products.objects.all()
    params = {
        'products' : products ,
    }
    return render(request , 'cart/home.html' , params )


def shop(request):
    products = Products.objects.all()
    params = {
        'products' : products ,
    }
    return render(request , 'cart/shop.html' , params)


def products(request , myid):
    allprods = Products.objects.all()  
    products = Products.objects.filter(id = myid)
    params = {
        'products' : products[0] , 
        'allprods' : allprods
    }
    return render(request , 'cart/products.html' , params)


def blog(request):
    return render(request , 'cart/blog.html')


def about(request):
    return render(request , 'cart/about.html')


def checkout(request):
    if request.method == 'POST' :
        items_json = request.POST.get('itemsJson' , '')
        name = request.POST.get('name' , '') 
        amount = request.POST.get('amount' , '') 
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        address = request.POST.get('address1' , '') + " " + request.POST.get('address2' , '')
        city = request.POST.get('city' , '')
        state = request.POST.get('state' , '')
        zip_code = request.POST.get('zip' , '')
        
        order = Order(items_json = items_json , name = name , email = email , phone = phone , address = address , city = city , state = state , zip_code = zip_code , amount = amount)
        order.save()
        update = OrderUpdate(order_id = order.order_id , update_desc = "The order has been placed")
        update.save()
        
        thank = True
        id = order.order_id
        return render(request , 'cart/checkout.html' , {'thank':thank , 'id': id})   
    return render(request , 'cart/checkout.html')     

def contact(request):
    if request.method == 'POST' :
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        subject = request.POST.get('subject' , '')
        description = request.POST.get('description' , '')    
        contact = Contact(name = name , email = email , phone = phone , subject = subject , description = description)
        contact.save()
        
        thank = True 
        id = contact.msg_id
        return render(request , 'cart/contact.html' , {'thank':thank , 'id': id})
    return render(request , 'cart/contact.html')


def tracker(request):
    if request.method == 'POST' :
        email = request.POST.get('email' , '')
        orderId = request.POST.get('orderId' , '')
        try :
            order = Order.objects.filter(order_id = orderId , email = email)
            if len(order)>0 :
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update :
                    updates.append({'text':item.update_desc , 'time':item.timestamp})
                    response = json.dumps([updates , order[0].items_json] , default=str)
                return HttpResponse(response)
            else :
               return HttpResponse('{}')
        except Exception as e   :
            return HttpResponse('{}')
    return render(request , 'cart/tracker.html') 


def cart(request):
    return render(request , 'cart/cart.html')

