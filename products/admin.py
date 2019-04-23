from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Category, CategoryAdmin)

# Register your models here.
admin.site.register(Product)