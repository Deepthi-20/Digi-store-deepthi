"""digitelstore1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users1 import views as v1
from admins1 import views as v2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.UA,name="UA"),
    path('categories/',v1.categories,name="categories"),
    path('alastview/', v2.alastview, name="alastview"),
    path('index/',v1.index,name='index'),
    path('register/',v1.register,name='register'),
    path('login/',v1.login,name='login'),
    path('profile/',v1.profile,name='profile'),
    path('home/',v1.home,name='home'),
    path('alogin/', v2.alogin, name='alogin'),
    path('addproduct/', v2.addproducts, name='addproduct'),
    path('viewproduct/', v2.viewproduct, name='viewproduct'),
    path('ahome/', v2.ahome, name='ahome'),
    path('profile1/', v2.profile1, name='profile1'),
    path('products/', v1.products, name='products'),
    path('buyproduct/<int:id>/buy/', v1.buyproduct, name='buyproduct'),
    path('purchase/', v1.purchase, name='purchase'),
    path('lastview/', v1.lastview, name='lastview'),
    path('logout/', v1.logout, name='logout'),
    path('alogout', v2.alogout, name='alogout'),
    path('contact/',v1.contact,name="contact"),
    path('last/', v1.last, name='last'),
    path('camera/',v1.camera,name='camera'),
    path('laptop/', v1.laptop, name='laptop'),
    path('mobile/', v1.mobile, name='mobile'),
    path('watch/', v1.watch, name='watch'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)