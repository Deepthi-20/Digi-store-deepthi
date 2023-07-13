from django.shortcuts import render, redirect
from .models import Register, Purchase
from admins.models import Products
from django.contrib import messages




# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'profile.html')

def register(request):
    if request.method=="POST":
        CNAME=request.POST.get('name')
        CEMAIL=request.POST.get('email')
        CPASSWORD=request.POST.get('password')
        CMOBILE=request.POST.get('mobile')
        CADDRESS=request.POST.get('address')
        CPINCODE=request.POST.get('pincode')
        data=Register(
            cname=CNAME,
            cemail=CEMAIL,
            paw=CPASSWORD,
            mno=CMOBILE,
            addr=CADDRESS,
            pincode=CPINCODE,
        )
        data.save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            password=request.POST.get('password')
            data = Register.objects.get(cemail=email,paw=password)
            request.session['userid'] = data.cemail
            print(data)
            return render(request,'home.html')
        except Exception as err:
            print("exception is:", err)
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def profile(request):
    try:
        uid = request.session['userid']
        print(uid)
        data = Register.objects.get(cemail=uid)
        return render(request,'profile.html',{'profile':[data]})
    except Exception as E:
        print("exception is:", E)
        return render(request, 'home.html')

def products(request):
    data = Products.objects.all()
    return render(request,'u_product.html',{'products':data})

def buyproduct(request,id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid = Register.objects.get(cemail=uid)
        product = Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcat,
            pcat=product.pcat,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=cid.id,
            pid_id=id
        )
        data.save()
        messages.success(request,'PURCHASED SUCCESSFULLY')
        return render(request, 'u_product.html')
    else:
        messages.error(request,'NOT PURCHASED>>CHECK IT')
        return redirect('products', id=id)

def purchase(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid)
    return render(request, 'u_purchase.html', {'data': data,'cdata':cdata})


def lastview(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request,'last_view.html',{'view':data,'cdata':cdata})


def logout(request):
    return render(request,'index.html')





def categories(request):
    return render(request,'categories.html')


def contact(request):
    return render(request,'contact.html')


def camera(request):
    return render(request,'camera.html')


def laptop(request):
    return render(request,'laptop.html')


def mobile(request):
    return render(request,'mobile.html')


def watch(request):
    return render(request,'watch.html')


def lp(request):
    return render(request,'lp.html')


def main(request):
    return render(request,'main.html')