from django.shortcuts import render, redirect
from ShoeApp.models import Checkout
from ShoeApp.models import Shoe
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def show(request):
    shoes = Shoe.objects.all()
    return render(request, "show.html", {'shoes': shoes})


def checkout(request, id):
    shoes = Shoe.objects.get(id=id)
    return render(request, "checkout.html", {'shoes': shoes})


def checkoutpay(request, id):
    shoes = Shoe.objects.get(id=id)
    if request.method == "POST":

        # capture input
        amount = shoes.price
        phoneNumber = request.POST.get('contact')

        # validation on the entries
        if not phoneNumber or not phoneNumber.isdigit():
            return HttpResponse("invalid phone number")
        if not amount or not amount.isdigit():
            return HttpResponse("invalid phone number")
        # Mpesa processes
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'CELESTIN ENTERPRISES'
        transaction_desc = 'Evanicela Payment'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkout.html", {'shoes': shoes})
