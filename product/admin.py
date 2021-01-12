from django.contrib import admin
from .models import Product , PorductImage ,Category, Product_Alternative, Product_Accessories
# Register your models here.

admin.site.register(Product)
admin.site.register(PorductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)