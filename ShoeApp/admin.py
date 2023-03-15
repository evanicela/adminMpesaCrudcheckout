from django.contrib import admin
from .models import Shoe
from .models import Checkout


# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('shoename', 'description', 'price', 'imageurl')


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('transactionid', 'amount', 'phone')


admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Checkout, CheckoutAdmin)
