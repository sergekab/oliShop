from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

from .models.orders import Order


#pour afficher les noms, prix, et la categorie de chaque produit dans django administration
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']



#cette ligne permet d'enregistrer un produit a partir de django administration
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)