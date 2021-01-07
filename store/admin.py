from django.contrib import admin
from store.models import Product,Category,Contact,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Order)
