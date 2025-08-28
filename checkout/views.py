from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})  # first will get the bag from the session
    if not bag:  # if there is nothing in the bag
        messages.error(request, "There's nothing in your bag at the moment")  # then add a simple error message
        return redirect(reverse('products'))  # and redirect back to the product page,will prevent people from typing/checkout

    order_form = OrderForm()  # create an instance of our order form, which will be empty for now
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51S13UMRuDxVCrrkHKyYaebiIv0j6IGMbDf68WYrkwOGLNs4F9EC5YSHROk4f72ELEo37ce9VKcoD5GXe5X0SJWsW00DsvvyXhh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
