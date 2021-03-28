
from django.contrib import admin
from .models import Register,categories,subcategories,products,carts,history,wish,payment

# Register your models here.
admin.site.register(Register)
admin.site.register(categories)
admin.site.register(subcategories)
admin.site.register(products)
admin.site.register(carts)
admin.site.register(history)
admin.site.register(wish)
admin.site.register(payment)




