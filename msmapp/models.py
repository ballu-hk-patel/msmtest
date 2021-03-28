from django.db import models
import datetime
from datetime import datetime


# Create your models here.


    
class Register(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    eadd = models.EmailField()
    cnumber = models.IntegerField()
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.fname


class categories(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class subcategories(models.Model):
    name = models.CharField(max_length=50, null=True)
    cname = models.ForeignKey(categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class products(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(subcategories, on_delete=models.CASCADE)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    p_type = models.CharField(max_length=22)
    image = models.ImageField(upload_to="media/", null=True)


    def __str__(self):
        return self.product_name


class wish(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    
    
class carts(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.BooleanField(default=False)

class history(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price = models.IntegerField()
    desc=models.CharField(max_length=200)
    added_time1 = models.DateTimeField(default=datetime.now, blank=True)

class payment(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    recipt=models.CharField(max_length=33,default="none")
    status = models.BooleanField(default=False)
    product_names=models.CharField(max_length=200)
    product_price=models.CharField(max_length=200)
    product_qun=models.CharField(max_length=200)
    product_img=models.CharField(max_length=200)
    total=models.CharField(max_length=200)

    



    
    