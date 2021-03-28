
from re import template
from django.conf.urls import static
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.core.mail import EmailMultiAlternatives 
from msm.settings import EMAIL_HOST_USER
import random
from django.conf import settings 

# Create your views h
def history11(request):
     if "is_logged" in request.session:
        user = Register.objects.get(eadd=request.session["is_logged"])
        print(user)
        r1=user.fname
        data=history.objects.filter(user_id=user.id)
        
        return render(request,"history.html",{"data":data,"user":r1})
        
def index(request):
    if "is_logged" in request.session:
        data = products.objects.all()
        customer_name = request.session.get("is_logged")
        r1 = Register.objects.get(eadd=customer_name)
        user=r1.fname
        
        return render(request, "index.html", {"data": data,"user":user})
    return render(request, "index.html")  


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact-us.html")


def about(request):
    return render(request, "about.html")


def shop(request):
    return render(request, "shop.html")


def wishlist(request):
    customer_name = request.session.get("is_logged")
    user = Register.objects.get(eadd=customer_name)
    wish11 = wish.objects.filter(user__id=user.id)
    return render(request, "wishlist.html", {"wish1": wish11 })


def sdetail(request):
    return render(request, "shop-detail.html")


def account(request):
    return render(request, "my-account.html")


def service(request):
    return render(request, "service.html")


def register(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        eadd = request.POST["eadd"]
        cnumber = request.POST["cnumber"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        pincode = request.POST["pincode"]
        city = request.POST["city"]
        password = request.POST["password"]

        reg = Register.objects.all()
        valid = Register(
            fname=fname,
            lname=lname,
            eadd=eadd,
            cnumber=cnumber,
            dob=dob,
            gender=gender,
            address=address,
            pincode=pincode,
            city=city,
            password=password,
        )
        valid.save()
        return redirect("/login")
    return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        # name = request.POST["name"]
        eadd = request.POST["eadd"]
        password = request.POST["password"]

        if Register.objects.filter(eadd=eadd, password=password):
            valid = Register.objects.get(eadd=eadd, password=password)
            print("*************************************************************")
            user_name=valid.fname
            request.session["is_logged"] = eadd
            v1 = "welcome"
            v = messages.error(request, " ")
            # return redirect("/index", {"v1": v1})
            return render(request, "index.html", {"v1": v1,"user":user_name})
        else:
            v1 = "not exist"
            v = messages.error(request, " ")
            return render(request, "login.html", {"v1": v1})
    return render(request, "login.html")


def logout(request):
    if 'is_logged' in request.session:
        del request.session['is_logged']
        return redirect('index')
    else:
        return redirect('/usernot')
    # del request.session["is_logged"]
    # return redirect("index")
def usernot(request):
    return render(request, "ar.html")  

# def cloth(request):
#     data = products.objects.all()
#     return render(request, "Clothing.html", {"data": data})


def elec(request, name):
    fcat = categories.objects.filter(name=name)
    prod = products.objects.filter(category_id=fcat[0].id)
    sub = subcategories.objects.filter(cname_id=fcat[0].id)
    return render(request, "electronic.html", {"prod": prod, "sub": sub})


def subelec(request, id):
    sub = subcategories.objects.filter()
    sm = subcategories.objects.filter(name=id)
    prod = products.objects.filter(subcategory_id=sm[0].id)
    return render(request, "electronic.html", {"sub": sub, "prod": prod})

s=[]
i=[0]
def men(request, name):
    fcat = categories.objects.filter(name=name)
    sub = subcategories.objects.filter(cname_id=fcat[0].id)
    prod = products.objects.filter(category_id=fcat[0].id)
    
    customer_name = request.session.get("is_logged")
    r1 = Register.objects.get(eadd=customer_name)
    user=r1.fname
    c1 = sub.count()
    cart = carts.objects.filter(user__id=r1.id)
    count=cart.count()
       
    if request.method == 'POST':
        if 'kind' in request.POST:
                se1=request.POST["se1"]
                se11=str(se1)
                s.append((se11))
                i.append((i[-1]+1))
                print(s)
                se_pro=products.objects.filter(category_id=fcat[0].id,p_type=se11)
                print(se_pro)
                return render(request, "men.html", {"prod": prod, "sub": sub,"se_pro":se_pro,"count":count,"user":user, "c1": c1})

    if 'price1' in request.POST:
                min1=request.POST["min"]
                max1=request.POST["max"]
                print(min1)
                print(max1) 
                if i[-1]%2==0:
                    s.pop(0)
                else:
                    pass    
                price_pro=products.objects.filter(category_id=fcat[0].id,price__range=(int(min1), int(max1)),p_type=s[-1])
                print(price_pro)
               
                return render(request, "men.html", {"prod": prod, "sub": sub,"price_pro":price_pro,"count":count,"user":user, "c1": c1})
    if 'ser1' in request.POST:
            # ========== Random Word Find ============= #
                qs=products.objects.all()
                title1=request.POST.get("search")
                if title1 != "" and title1 is not None:
                    qs=qs.filter(product_name__icontains=title1)
                    cou1=qs.count()
                    print(cou1)
                    # ===== second type of filter for search
                    # cou1=products.objects.filter(product_name__icontains=title1)
                    # print("===========")
                    # cou1=cou1.count()
                    # print(cou1)
                    return render(request,"men.html",{"qs":qs,"sub": sub,"count":count,"user":user, "c1": c1,"cou1":cou1})
                else:
                    search_err="not found !"    
                    return render(request,"men.html",{"search_err":search_err,"sub": sub,"count":count,"user":user, "c1": c1})

                # ====== Exact Product Name =========== #
                # se1=request.POST["search"]
                # se1=str(se1)
                # print(se1) 
                # if products.objects.filter(product_name=se1):
                #     search_pro=products.objects.filter(product_name=se1)
                #     print(search_pro)
                #     return render(request, "men.html", { "sub": sub,"count":count,"user":user, "c1": c1})
                # else:
                #     search_err="Not Found " +"\"" + se1 +"\""
                #     print(search_err)
                #     return render(request, "men.html", {"search_err":search_err, "sub": sub,"count":count,"user":user, "c1": c1}) 
            # return render(request, "men.html", {"prod": prod,"search_err":search_err, "sub": sub,"search_pro":search_pro,"count":count,"user":user, "c1": c1})                   
    else:
                pass    
    
    return render(request, "men.html", {"prod": prod, "sub": sub,"count":count,"user":user, "c1": c1})

def submen(request, id):
    sub = subcategories.objects.filter()
    sm = subcategories.objects.filter(name=id)
    prod = products.objects.filter(subcategory_id=sm[0].id)
    if request.method == 'POST':
            if 'kind' in request.POST:
                se1=request.POST["se1"]
                se1=str(se1)
                print(se1)
                se_pro=products.objects.filter(subcategory_id=sm[0].id,p_type=se1)
                print(se_pro)
                return render(request, "men.html", {"prod": prod, "se_pro":se_pro,})

            elif 'price1' in request.POST:
                min1=request.POST["min"]
                max1=request.POST["max"]
                print(min1)
                print(max1) 
                price_pro=products.objects.filter(subcategory_id=sm[0].id,price__range=(int(min1), int(max1)))
                print(price_pro)
                return render(request, "men.html", {"prod": prod, "price_pro":price_pro,})           
            else:
                pass    
    return render(request, "men.html", { "prod": prod})



def women(request, name):
    fcat = categories.objects.filter(name=name)
    prod = products.objects.filter(category_id=fcat[0].id)
    sub = subcategories.objects.filter(cname_id=fcat[0].id)
    if "is_logged" in request.session:
        customer_name = request.session.get("is_logged")
        r1 = Register.objects.get(eadd=customer_name)
        user=r1.fname
        
        cart = carts.objects.filter(user__id=r1.id)
        count=cart.count()
        print(count)
        c1 = sub.count()
        print(c1)
        data = serializers.serialize("json", cart)
        return render(request, "men.html", {"prod": prod, "sub": sub,"count":count,"user":user,"c1":c1})
    return render(request, "women.html", {"prod": prod, "sub": sub})


def subwomen(request, id):
    sub = subcategories.objects.filter()
    sm = subcategories.objects.filter(id=id)
    prod = products.objects.filter(subcategory_id=sm[0].id)
    return render(request, "women.html", { "prod": prod})


def kitchen(request, name):
    fcat = categories.objects.filter(name=name)
    prod = products.objects.filter(category_id=fcat[0].id)
    sub = subcategories.objects.filter(cname_id=fcat[0].id)
    return render(request, "kitchen.html", {"prod": prod, "sub": sub})


def subkitchen(request, id):
    sub = subcategories.objects.filter()
    sm = subcategories.objects.filter(name=id)
    prod = products.objects.filter(subcategory_id=sm[0].id)
    return render(request, "kitchen.html", {"sub": sub, "prod": prod})


def baby(request, name):
    fcat = categories.objects.filter(name=name)
    prod = products.objects.filter(category_id=fcat[0].id)
    sub = subcategories.objects.filter(cname_id=fcat[0].id)
    return render(request, "baby.html", {"prod": prod, "sub": sub})


def subbaby(request, id):
    sub = subcategories.objects.filter()
    sm = subcategories.objects.filter(name=id)
    prod = products.objects.filter(subcategory_id=sm[0].id)
    return render(request, "baby.html", {"sub": sub, "prod": prod})

def dele(request,id):
    if "is_logged" in request.session:
        product=products.objects.get(id=id)
        user=Register.objects.get(eadd=request.session["is_logged"])
        cart=carts.objects.filter(user_id=user.id,product_id=product.id)

        del cart
        carts.objects.filter(user_id=user.id,product_id=product.id).delete()
        return redirect('cart')
    return render(request,"cart.html")    

def dele_his(request,id):
    if "is_logged" in request.session:
        his=history.objects.filter(id=id)

        del his
        history.objects.filter(id=id).delete()
        return redirect('history')
    return render(request,"history.html")     

def wish1(request,id):
    product=products.objects.get(id=id) 
    name=product.product_name
    price=product.price
    desc=product.desc
    
    #  add wishlist
    if "is_logged" in request.session:
        if not  wish.objects.filter(product_name=name):
            user = Register.objects.get(eadd=request.session["is_logged"])
            wish1=wish.objects.filter(user_id=user.id)
            wish1 = wish(
                            user_id=user.id,
                            product_name=name,
                            price=price,
                            desc=desc,
                        )
            wish1.save()
            print("done")
        else:
            pass    
    return redirect(request.META['HTTP_REFERER'])    
    # return HttpResponse(" added successfully done")
    # if "is_logged" in request.session:
    #     customer_name = request.session.get("is_logged")
    #     r1 = Register.objects.get(eadd=customer_name)
    #     print(r1)
        
    #     cart = carts.objects.filter(user__id=r1.id)
    #     data = serializers.serialize("json", cart)
 
        
    # else:
    #     pass    

def sdetail(request,id):
    product=products.objects.get(id=id) 
    id1=product.id
    name=product.product_name
    price = product.price
    cat=product.category
    desc=product.desc
    type1=product.p_type
    img=product.image
    product = products.objects.get(id=id)
    user = Register.objects.get(eadd=request.session["is_logged"])

    #  visit page (create History)
    
    his=history.objects.filter(user_id=user.id, product_id_id=product.id)
    his = history(
                    user_id=user.id,
                    product_id_id=product.id,
                    product_name=product.product_name,
                    price=product.price,
                    desc=product.desc,
                )
    his.save()
    print("done")

    if request.method == "POST":
         q1= request.POST["quantity"] 
         q1=int(q1)
         print(q1)
         if "is_logged" in request.session:
            print(request.session["is_logged"])
            product = products.objects.get(id=id)
            user = Register.objects.get(eadd=request.session["is_logged"])
            print(user.id)

            cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
            count = carts.objects.filter(user_id=user.id, product_id_id=product.id).count()

            if count > 0:
                cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
                qty = q1
                t_price = qty * round(product.price,2)
                carts.objects.filter(user_id=user.id, product_id_id=product.id).update(quantity=qty, price=t_price)
                return redirect("cart")

            else:
                print("@@@@@@", user.id)
                cart = carts(
                    user_id=user.id,
                    product_id_id=product.id,
                    quantity=q1,
                    price=product.price*q1,
                )

                cart.save()
                return redirect("cart")
    return render(request,"shop-detail.html",
            {"name":name,"price":price,"img":img,"cat":cat,"desc":desc,"type1":type1,"id1":id1})

def show_data(request,id):
    product=products.objects.get(id=id) 
    name=product.product_name
    price = product.price
    cat=product.category
    desc=product.desc
    type1=product.p_type
    img=product.image
    product = products.objects.get(id=id)
    user = Register.objects.get(eadd=request.session["is_logged"])

    #  visit page (create History)
    his=history.objects.filter(user_id=user.id, product_id_id=product.id)
    his = history(
                    user_id=user.id,
                    product_id_id=product.id,
                    product_name=product.product_name,
                    price=product.price,
                    desc=product.desc,
                )
    his.save()
    print("done")

    # AI Base Show Product
    name_key=name.split()
    print(name_key)
    name_key=name_key[0]
    qs=products.objects.filter(product_name__icontains=name_key)[:9]
    print(qs)

    # Add To Cart Funcation
    if request.method == "POST":
         q1= request.POST["quantity"] 
         q1=int(q1)
         print(q1)
         if "is_logged" in request.session:
            print(request.session["is_logged"])
            product = products.objects.get(id=id)
            user = Register.objects.get(eadd=request.session["is_logged"])
            print(user.id)

            cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
            count = carts.objects.filter(user_id=user.id, product_id_id=product.id).count()

            if count > 0:
                cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
                qty = q1
                t_price = qty * round(product.price,2)
                carts.objects.filter(user_id=user.id, product_id_id=product.id).update(quantity=qty, price=t_price)
                return redirect("cart")

            else:
                print("@@@@@@", user.id)
                cart = carts(
                    user_id=user.id,
                    product_id_id=product.id,
                    quantity=q1,
                    price=product.price*q1,
                )

                cart.save()
                return redirect("cart")
         else:
            return redirect("login")
    
         
    return render(request,"show_data.html",
            {"name":name,"price":price,"img":img,"cat":cat,"desc":desc,"type1":type1,"qs":qs})


def order(request):
    p11=[]
    co1="success"
    co2="warning"
    if "is_logged" in request.session:
        user = Register.objects.get(eadd=request.session["is_logged"])
        n=user.fname
        cart = carts.objects.filter(user_id=user.id)
        all_prod=[]
        for i in cart:
            product = products.objects.filter(id=i.product_id_id)
            print(product)
            all_prod.extend(product)
            p11.append(i.price) 

        print(all_prod[0])    
        total = sum(p11)
        dis=total-((total*10)/100)
        gst=((total*2)/100)
        all=round(dis+gst,2)
        print(all)
        cart1=zip(all_prod,cart)
        
        return render(request,"order.html",{"cart":cart1,"total":total,"all":all,"n":n,"p11":p11,"all_prod":all_prod,"co1":co1,"co2":co2})

# def outer(request):
#     cart=carts.objects.get(id=48)
#     print(cart.product_id)
#     print(cart.quantity)
#     print(cart.price)

#     return render(request,"base.html")
def outer_add_cart(request,id):
    
    if "is_logged" in request.session:
        if request.method == "POST":
            q1= request.POST.get('quantity') 
            q1=int(q1)
            print(f"{q1}`````")
            print(id)
            
            product = products.objects.get(id=id)
            user = Register.objects.get(eadd=request.session["is_logged"])
            print("==============================================")
            print(user.id)

            cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
            qty =q1 
            t_price = qty * product.price
            carts.objects.filter(user_id=user.id, product_id_id=product.id).update(quantity=qty, price=t_price)
            return redirect("cart")
    return redirect("cart")    
       
def add_cart(request, id):
    if "is_logged" in request.session:
        print(request.session["is_logged"])
        product = products.objects.get(id=id)
        user = Register.objects.get(eadd=request.session["is_logged"])
        print(user.id)

        cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
        count = carts.objects.filter(user_id=user.id, product_id_id=product.id).count()

        if count > 0:
            cart = carts.objects.filter(user_id=user.id, product_id_id=product.id)
            qty = cart[0].quantity + 1
            t_price = qty * product.price
            carts.objects.filter(user_id=user.id, product_id_id=product.id).update(
                quantity=qty, price=t_price
            )
            return redirect("cart")

        else:
            print("@@@@@@", user.id)
            cart = carts(
                user_id=user.id,
                product_id_id=product.id,
                quantity=1,
                price=product.price,
            )
            cart.save()
            return redirect("cart")
    else:
        return redirect("login")


def cart(request):
    if "is_logged" in request.session:
        user = Register.objects.get(eadd=request.session["is_logged"])
        print(user)

        cart = carts.objects.filter(user__id=user.id)
        count = carts.objects.filter(user__id=user.id).count()
        data = serializers.serialize("json", cart)
        plus=cart.count()
        plus1=list(range(1, plus+1))
        print(plus1)
        
        all_prod = []
        totalprice = []
        q1=0

        for i in cart:
            totalprice.append(i.price)
            q1=int(i.quantity)
            product = products.objects.filter(id=i.product_id_id)
            all_prod.extend(product)
            
        total = sum(totalprice)
        dis=total-((total*10)/100)
        gst=((total*2)/100)
        total_all=round(dis+gst,2)
        print(total)
        
        cart1 = zip(all_prod, cart,plus1)
        return render(
            request, "cart.html", {"q1":q1,"cart": cart1,"count":count, "total": total,"total_all":total_all, "data": data}
        )
    else:
        return redirect("login")

def pay1(request):
    if "is_logged" in request.session:
        user = Register.objects.get(eadd=request.session["is_logged"])
        print(user)

        cart = carts.objects.filter(user__id=user.id)
        count = carts.objects.filter(user__id=user.id).count()
        data = serializers.serialize("json", cart)

        product_names= []
        product_price_i = []
        product_price_s = []
        product_qun=[]
        product_img=[]
        total=[]
        all_prod=[]
        status=[]
        for i in cart:
            product_price_s.append(str(i.price))

        for i in cart:
            product = products.objects.filter(id=i.product_id_id)
            all_prod.extend(product)
        for i in all_prod:
            w=str(i.image)
            xx=w.split("/")
            print(xx[1])
            product_img.append(w)
            print(w)    

        for i in cart:
            product_price_i.append(i.price)
            status.append(i.status)
            product_qun.append(str(i.quantity))
            product1= products.objects.filter(id=i.product_id_id)
            product_names.extend(product1)
        print(product_img)
        total = sum(product_price_i) 
        recipt="order_101_2355"
          

        #convert string
        pn_str=""
        pp=(','.join(product_price_s))
        pq=(','.join(product_qun))
        pi=(','.join(product_img))
        
        
        for i in cart:
            product = products.objects.filter(id=i.product_id_id)
            for i in product:
                p=str(i)+','
                pn_str+=p
        print(pn_str)
        print(pp)
        print(pq)
        if not payment.objects.filter(user__id=user.id,recipt=recipt):
            p1=payment(
                user_id=user.id,
                recipt=recipt,
                product_names=pn_str,
                product_price=pp,
                product_qun=pq,
                total=total,
                product_img=pi
                
            )
            p1.save()
        #after show
        
        if payment.objects.filter(user__id=user.id):
                cc=payment.objects.filter(user__id=user.id).count()
                cc=cc-1
                qq=payment.objects.filter(user__id=user.id)[cc]
                aa=qq.product_names
                aa=aa.split(",")
                print(type(aa))
                bb=qq.product_price
                bb=bb.split(",")
                print(type(bb))
                cc=qq.product_qun
                cc=cc.split(",")
                print(type(cc))
                dd=str(qq.status)
                ee=str(qq.product_img)
                print(ee)
                cart1 = zip(aa,bb,cc,all_prod)
         

              
    return render(request,"order1.html",{"cart":cart1,"s":dd})

            # totalprice.append(i.price)
            # q1=int(i.quantity)
            # product = products.objects.filter(id=i.product_id_id)
            # all_prod.extend(product)



def randome(request):
    qs=products.objects.all()
    title1=request.POST.get("ser1")
    if title1 != "" and title1 is not None:
        qs=qs.filter(product_name__icontains=title1)
        
    else:
        qs_error="not found !"    
    cou1=qs.count()
    context={
        "queryset":qs,
        "cou1":cou1,
        
        
    }    
    return render(request,"randome.html",context)

def otp():
    otp_user=random.randint(1000,9999)
    return otp_user
a=[]
def test(request):    
    if request.method == 'POST':
        if 'email1' in request.POST:
            
                otp_user=random.randint(1000,9999)
                a.append(otp_user)
                print(otp_user)
                e1=request.POST.get("email")
                if Register.objects.filter(eadd=e1):

                    msg=EmailMultiAlternatives(f'otp from msm app',f'{otp_user}',EMAIL_HOST_USER,[f'{e1}'])
                    msg.send()
                    return render(request,"test.html",{"otp":otp_user})
                else:
                    not_user="not user match"
                    return render(request,"test.html",{"not_user":not_user})    
                
    if 'otp1' in request.POST:
        print(a)
        print(a[-1])
        o1=request.POST["otp"]
        if int(a[-1]) == int(o1):
            print("done")
            msg="done"
            return render(request,"test.html",{"msg":msg})  
        else:
            print("error")
            msg="error plz enter valid otp (agian enter email)"  
            return render(request,"test.html",{"msg":msg}) 

    if 'change' in request.POST:
        e11=request.POST["e1"]
        c11=request.POST["c1"]
        if Register.objects.filter(eadd=e11):
            valid = Register.objects.get(eadd=e11)
            Register.objects.filter(eadd=e11).update(password=c11)
            done="password sucessfully change"
            return render(request,"test.html",{"done":done})
        else:
            done="not set a password! plz valid email"
            return render(request,"test.html",{"done":done})    

    return render(request,"test.html")

def from1(request):
    if request.method == "POST":
        name=request.POST["fname"]
        no=request.POST["no"]
        cvv=request.POST["cvv"]
        if name !="" and 14 == len(no) and 3 == len(cvv):
            msg="done somthing"

            return redirect("test")
        else:
            msg="wrong somthing"
            return render(request,"from1.html",{"msg":msg})
    return render(request,"from1.html")


#urls and msmapp urls(optional)
#pdf1.html
#customer.html
#mathfilter install, add settings ,and import html file
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from io import BytesIO
import datetime
class CustomerListView(ListView):
    model=payment
    template_name='test.html'

def fetch_resources(uri, rel):
    import os.path
    from django.conf import settings
    path = os.path.join(
            settings.STATICFILES_DIRS ,
            uri.replace(settings.STATIC_URL, ""),
            settings.MEDIA_ROOT,
            uri.replace(settings.MEDIA_URL, ""))
    return path
def customer_render(request,*args,**kwargs):
    template_path = 'pdf1.html'
    #data-created
    all_prod=[]
    user = Register.objects.get(eadd=request.session["is_logged"])
    cart = carts.objects.filter(user__id=user.id)
    for i in cart:
            product = products.objects.filter(id=i.product_id_id)
            all_prod.extend(product)
    if payment1.objects.filter(user__id=user.id):
                user=checkout.objects.get(eadd=request.session["is_logged"])
                name1=user.fname
                add1=user.address
                
                cc=payment1.objects.filter(user__id=user.id).count()
                cc=cc-1
                qq=payment1.objects.filter(user__id=user.id)[cc]
                aa=qq.product_names
                aa=aa.split(",")
                print(type(aa))
                bb=qq.product_price
                bb=bb.split(",")
                print(type(bb))
                cc=qq.product_qun
                cc=cc.split(",")
                print(type(cc))
                dd=str(qq.status)
                print(dd)
                ee=str(qq.product_img)
                ee=ee.split(",")
                print(ee)
                total=qq.total
                r=qq.recipt
                now = datetime.datetime.now()
                date1=now.strftime("%Y-%m-%d %H:%M:%S")
                cart1 = zip(aa,bb,cc,ee,all_prod)
    context = {'data': cart1,"total":total,"r":r,"date":date1,"name":name1,"add":add1}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Mihira_reciept_101.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,link_callback=fetch_resources)

    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
 