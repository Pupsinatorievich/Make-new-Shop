from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.
#==============================================================

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    
#==============================================================
    
class ProductAdmin(admin.ModelAdmin):

    list_display = [fields.name for fields in Product._meta.fields]
    inlines = [ProductImageInline]
 
    class Meta:
        model = Product        
admin.site.register(Product, ProductAdmin)  

#==============================================================

class ProductImageAdmin(admin.ModelAdmin):

    list_display = [fields.name for fields in ProductImage._meta.fields]
 
    class Meta:
        model = ProductImage       
admin.site.register(ProductImage, ProductImageAdmin)  