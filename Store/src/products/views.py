from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator
from . filters import ProductsFilter
from . models import *
from django.http import JsonResponse
import json
import datetime
from . utils import  getCookie,cookieData,gestOrder



def products_list(request):
    data=cookieData(request)
    customerItem=data['customerItem']
    prod_list=Product.objects.all()
    myfilter=ProductsFilter(request.GET,queryset=prod_list)
    prod_list=myfilter.qs

    paginator=Paginator(prod_list, 6)
    page_number=request.GET.get('page')
    prod_list=paginator.get_page(page_number)

    context={'prod_list':prod_list , 'myfilter':myfilter, 'customerItem':customerItem ,'shipping':False}
    return render(request,'products/prodects_list.html',context)

###################

def product_detail(request,slug):
    detail=get_object_or_404(Product,PRDSlug=slug)
    context={'detail':detail}
    return render(request,'products/product_detail.html',context)

##################

def cart(request):
    data=cookieData(request)
    items=data['items']
    order=data['order']
    customerItem=data['customerItem']
    context={'items':items, 'order':order ,'customerItem':customerItem}
    context={'items':items, 'order':order ,'customerItem':customerItem}
    return render(request,'products/cart.html',context)

#############

def checkout(request):
    data=cookieData(request)
    items=data['items']
    order=data['order']
    customerItem=data['customerItem']
    context={'items':items, 'order':order ,'customerItem':customerItem}
    return render(request,'products/checkout.html',context)


#####################

def updateItem(request):
    data=json.loads(request.body)
    productID=data['productID']
    action=data['action']
    producte=Product.objects.get(id=productID)
    customer=request.user
    order , created=Order.objects.get_or_create(customer=customer, complate=False)
    orderItem , created=OrderItems.objects.get_or_create(order=order, producte=producte)

    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity=(orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()

    print('ptoductId :' ,productID)
    print('Action :', action)
    return JsonResponse('item was added',safe=False)

def addAndRemovItem(request):
    data=json.loads(request.body)
    productId=data['productID']
    action=data['action']
    print('productId' ,productId)
    print('Action :', action)
    customer=request.user
    order,created=Order.objects.get_or_create(customer=customer,complate=False)
    orderitem,created=OrderItems.objects.get_or_create(order=order,producte=productId)
    if action == 'add':
        orderitem.quantity=(orderitem.quantity + 1)
    elif action == 'remove' :
        orderitem.quantity=(orderitem.quantity - 1)
    orderitem.save()
    if orderitem.quantity <=0 :
        orderitem.delete()
    return JsonResponse('data was changed' , safe=False)

def processOrder(request):
    transction_Id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer ,complate=False)

    else:
        customer,order=gestOrder(request,data)
    total=float(data['form']['total'])
    print(total)
    order.transaction_id=transction_Id
    if total == float(order.get_total_items) :
        order.complate=True
    order.save()
    if order.shipping == True :
        ShippingAderess.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment submmited' , safe=False)
