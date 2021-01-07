from django.shortcuts import render
from store.models import Product,Category,Contact,Order
from math import ceil
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'store/index.html',{'product':product,'category':category})



def about(request):
    return render(request,'store/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'store/contact.html')


def tracker(request):
    return render(request,'store/tracker.html')




def search(request):
    product = Product.objects.all()
    category = Category.objects.all()
    if request.method == "POST":
        srch = request.POST.get('srch')
        # print('this isfrom search '+ srch)
        if srch:
            match = Product.objects.filter(Q(product_name__icontains = srch) |
                                         Q(desc__icontains = srch) 
                                          )
            if match:
                return render(request,'store/search.html',{"match":match})
        # else:
        # #    return render(request,'store/search.html',{'product':product,'category':category})
        #     HttpResponse('nhai hua ')
    
    return render(request,'store/index.html',{'product':product,'category':category})
    # return render(request,'store/index.html')



def productview(request,id):
    product = Product.objects.filter(id=id)
    return render(request,'store/productview.html',{'product':product})




def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get('item_json','') 
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('add1','') + request.POST.get('add2','')
        city = request.POST.get('city','')
        zip_code = request.POST.get('name','')
        state = request.POST.get('name','')
        
        order = Order(item_json= item_json,name= name,email=email, address= address,city = city ,zip_code=zip_code,state= state )
        order.save()
        thank = True
        id = order.order_id
        return render(request,'store/checkout.html',{'thank':thank,"id":id})

    return render(request,'store/checkout.html')



