from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.contact import Contact

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','time']
    search_fields = ['name']



class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','password']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','message']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer, AdminCustomer )
admin.site.register(Contact, AdminContact )

#, AdminProduct