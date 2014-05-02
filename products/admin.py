from django.contrib import admin
from models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price' ]


admin.site.register(Product,ProductAdmin)
