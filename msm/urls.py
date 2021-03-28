"""msm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from os import name
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from msmapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    # path("pdf/",views.render_pdf_view,name="test_view"),
    path("main_pdf/",views.CustomerListView.as_view(),name="main_pdf"),
    path("pdf1/",views.customer_render,name="customer_render_view"),
    path("cart/", views.cart, name="cart"),
    path("wish1/<str:id>", views.wish1, name="wish1"),
    path("checkout/", views.checkout, name="checkout"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    # path("test/",views.outer,name="test"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("sdetail/<str:id>", views.sdetail, name="sdetail"),
    path("account/", views.account, name="account"),
    path("service/", views.service, name="service"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("usernot/",views.usernot,name="usernot"),
    # path("cloth/", views.cloth, name="cloth"),
    path("elec/<str:name>", views.elec, name="elec"),

    path("men/<str:name>", views.men, name="men"),
    path("women/<str:name>", views.women, name="women"),
    path("kitchen/<str:name>", views.kitchen, name="kitchen"),
    path("baby/<str:name>", views.baby, name="baby"),
    path("submen/<str:id>", views.submen, name="sub1"),
    path("show_data/<str:id>", views.show_data, name="show_data"),
    path("history/", views.history11, name="history"),
    # path("men/<str:name>", views.fil, name="fil"),


    path("subwomen/<int:id>", views.subwomen, name="sub1"),
    path("subelec/<str:id>", views.subelec, name="sub1"),
    path("subkitchen/<str:id>", views.subkitchen, name="sub1"),
    path("subbaby/<str:id>", views.subbaby, name="sub1"),
    path("outer_add_cart/<str:id>", views.outer_add_cart, name="outer_add_cart"),

    path("add_cart/<str:id>", views.add_cart, name="add_cart"),
    path("cart/", views.cart, name="cart"),
    path("randome/", views.randome, name="randome"),
    path("test/", views.test, name="test"),
    path("from1/", views.from1, name="from1"),
    # path("add_history/<int:id>", views.add_history, name="add_history"),
    # path("history/", views.history, name="history"),
    path("order/", views.order, name="order"),
    path("pay1/", views.pay1, name="pay1"),
    path("cart/<str:id>", views.dele, name="dele"),
    path("history/<str:id>",views.dele_his,name="dele_his"),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)