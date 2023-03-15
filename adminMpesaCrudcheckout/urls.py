from django.contrib import admin
from django.urls import path
from ShoeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show),
    path('show',views.show),
    path('checkout/<int:id>',views.checkout),
    path('checkoutpay/<int:id>',views.checkoutpay)
]