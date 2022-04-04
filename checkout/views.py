from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KjjHRBSnuoi0bmQg3YZJgOPpeDurILqJAi5WCYdzeQ4wYbOp2HU0YvW8QcvT6sIbPrRzuVaZ6Tevj9e8M4GK1Fb00M4ax5fpP',
        'client_secret': "test client secret"
    }

    return render(request, template, context)
