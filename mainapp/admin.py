from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','slug','name','video','img')
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['img']




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','category','p_name','p_price','slug','p_img','p_des','p_max','p_min')
    prepopulated_fields = {'slug':('p_name',)}


  









