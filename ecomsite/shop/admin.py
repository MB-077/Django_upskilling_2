from django.contrib import admin
from .models import *

admin.site.site_header = "E-commerce Site Admin"
admin.site.site_title = "E-commerce Site Admin Portal"
admin.site.index_title = "Welcome to E-commerce Site Admin Portal"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category',)
    search_fields = ('title', 'category',)
    list_filter = ('category',)
    
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    
    change_category_to_default.short_description = 'Default Category' 
        
    actions = ('change_category_to_default',)
    fields = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    list_editable = ('price', 'category')
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
