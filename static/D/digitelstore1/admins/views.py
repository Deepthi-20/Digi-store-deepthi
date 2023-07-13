from django.shortcuts import render
from .models import Products
from user.models import Register, Purchase
from  django.core.files import File
from PIL import Image


def alogin(request):
    if request.method=='POST':
        try:
            aemail=request.POST.get('email')
            apassword=request.POST.get('password')
            if aemail=='sai@gmail.com' and apassword=='1919':
                return render(request,'a_home.html')
            else:
                return render(request,'a_login.html')
        except Exception as err:
            print("EXCEPTION IS:",err)
            return render(request,'a_login.html')
    else:
        return render(request,'a_login.html')




def viewproduct(request):
    data = Products.objects.all()
    print(data)
    return render(request, 'viewproducts.html', {'data': data})


def a_logout(request):
    return render(request,'a_home.html')



def addproducts(request):
    if request.method=='POST':
        try:
            pname=request.POST.get('pname')
            pcat= request.POST.get('pcat')
            pcost= request.POST.get('pcost')
            pquality= request.POST.get('pquality')
            pdec= request.POST.get('pdec')
            pimage=request.FILES['pimage']
            print(pimage)

            data=Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,
            )
            data.save()
            return render(request,'viewproducts.html')
        except Exception as err:
            print("EXCEPTION is:",err)
            return render(request,'a_home.html')
    else:
            return render(request, 'addproduct.html')

def ahome(request):
    return render(request, 'a_home.html')


def profile1(request):
    try:
        data=Products.objects.all()
        return render(request,'viewproducts.html',{'profile4':[data]})
    except Exception as err:
        print("EXCEPTION IS:",err)
        return render(request,'addproduct.html')


def alogout(request):
    return render(request,'a_home.html')