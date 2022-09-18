from django.shortcuts import render,redirect
#importing the models
from .models import MenuCategory, MenuItem ,ClientReview,RestaurantInfo,ComingSoon

import urllib.parse

# Create your views here.




# Home function
def home(request):
    # create a session for the cart
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    # print cart
    cart=[]
    cart_total=0
    cart_nbr=0
    #url encode 
    # order ="Hi, this message is from Guemmoune website.\n i would like to order :\n"
    for i in request.session['cart']:
        if request.session['cart'][i]['name'] is not None:
            cart.append(request.session['cart'][i])
            cart_total+=float(request.session['cart'][i]['total_price'])
            cart_nbr +=1
    #         #get order message
    #         order +="\n      ##"+str(request.session['cart'][i]['name'])+ " | "+str(request.session['cart'][i]['price']) + " x "+str(request.session['cart'][i]['quantity'])

    # order+="\n    # -> Total of "+str(cart_total)
  
    # wp_msg=urllib.parse.quote(order)
   
    # get all menu categories 
    categories = MenuCategory.objects.all()
    # get all menu items
    items = MenuItem.objects.all()
    #get all reviews
    reviews = ClientReview.objects.all()
    #get restaurant info the first
    restaurant = RestaurantInfo.objects.first()
    #get coming soon items
    coming_soon = ComingSoon.objects.all()



    # render the home page
    return render(request, 'index.html', {'categories': categories, 'items': items,'cart':cart,'cart_total':cart_total,'cart_nbr':cart_nbr,'reviews':reviews,'restaurant':restaurant,'coming_soon':coming_soon})



# add to cart function
def add_to_cart(request, id):
    # get the item
    item = MenuItem.objects.get(id=id)
    # get the item id
    item_id = str(item.id)
    # get the item name
    item_name = item.name
    # get the item price
    item_price = item.price
    # show variable modale
    
    # add the item to the cart
    # if the item is already in the cart
    if item_id in request.session['cart']:
        # increase the quantity by 1
        request.session['cart'][item_id]['quantity'] += 1
        # and update the total price
        request.session['cart'][item_id]['total_price'] = str(float(item_price) * float(request.session['cart'][item_id]['quantity']))
    # if the item is not in the cart
    else:
        # add the item to the cart
        request.session['cart'][item_id] = {'id':item_id,'name':item_name, 'price':str(item_price), 'quantity':1, 'total_price':str(item_price)}
    request.session.modified = True
    
    # redirect to home

    return redirect('Home')

# delete from cart function
def delete_from_cart(request, id):
    # get the item id
    item_id = str(id)
    # delete the item from the cart
    del request.session['cart'][item_id]
    request.session.modified = True
    # redirect to home
    return redirect('Home')

# checkout function
def checkout(request):
    # get name and adress and  from the form
    name = request.POST['name']
    adress = request.POST['adress']
    #get the selected radio button value form the form
    payment = request.POST['payment']

    # get the cart
    cart = request.session['cart']
    # get the cart total
    cart_total = 0
    # get the firs phone number from RestaurantInfo
    phone = RestaurantInfo.objects.first().phone

    for i in cart:
        cart_total += float(cart[i]['total_price'])
    # send the order on whatsapp as link
    # make the order message as template
    order = "Hi, this message is from Guemmoune website.\n i would like to order :\n"
    # add the order items to the message
    for i in cart:
        order += "\n      ##"+str(cart[i]['name'])+ " | "+str(cart[i]['price']) + " x "+str(cart[i]['quantity'])
    # add the total to the message
    order += "\n    # -> Total of "+str(cart_total)
    # add the name and adress to the message
    order += "\n    # -> Name : "+str(name)
    order += "\n    # -> Adress : "+str(adress)
    # add the payment method to the message
    order += "\n    # -> Payment : "+str(payment)
    # encode the message
    wp_msg = urllib.parse.quote(order)
    # make the whatsapp link
    wp_link = "https://api.whatsapp.com/send?phone="+str(phone)+"&text="+wp_msg
    # redirect to the whatsapp link
    return redirect(wp_link)
    