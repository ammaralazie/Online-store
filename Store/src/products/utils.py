import json
from . models import *
def  getCookie(request):
    try:
        cart=json.loads(request.COOKIES['cart'])
        print('cart : ',cart)
    except:
        cart={}
    print('cart : ',cart)
    items=[]
    order={'get_total_price':0 ,'get_total_items':0 ,'shipping':False}
    customerItem=order['get_total_items']
    try:
        for i in cart:
            customerItem +=cart[i]['quantity']
            product=Product.objects.get(id=i)

            total=product.PRDPrice *cart[i]['quantity']
            cart[i]['quantity']
            order['get_total_price']+=total
            order['get_total_items']+=cart[i]['quantity']
            item={

            'producte':{
            'id':product.id,
            'PRDName':product.PRDName,
            'PRDPrice':product.PRDPrice,
            'PRDImage':product.PRDImage,
            },
            'quantity':cart[i]['quantity'],
            'get_total':total
            }
            items.append(item)
            if product.PRDDigital == False:
                order['shipping'] = True
    except:
        pass
    return {'items':items, 'order':order ,'customerItem':customerItem}

##############################

def cookieData(request):
    if request.user.is_authenticated :
        customer=request.user
        order, ceated=Order.objects.get_or_create(customer=customer,complate=False)
        items=order.orderitems_set.all()
        customerItem=order.get_total_items
    else :
        getCookieData=getCookie(request)
        items=getCookieData['items']
        order=getCookieData['order']
        customerItem=getCookieData['customerItem']

    return{'items':items, 'order':order ,'customerItem':customerItem}

####################

def gestOrder(request,data):
    print('sorry this user is not authenticate plase login')
    name=data['form']['name']
    email=data['form']['email']
    coo=getCookie(request)
    items=coo['items']
    customer,created=User.objects.get_or_create(username=name)
    customer.email=email
    customer.save()
    order=Order.objects.create(customer=customer,complate=False)
    for item in items :
        product=Product.objects.get(id=item['producte']['id'])
        orderItems=OrderItems.objects.create(
            producte=product,
            order=order,
            quantity=item['quantity']
        )
    return customer,order
