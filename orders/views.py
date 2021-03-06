from django.shortcuts import render
from django.core.mail import send_mail

from store.models import OrderItem
from store.forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product = item['product'],
                    price = item['price'],
                    quantity = item['quantity']
                )
            cart.clear()
            send_mail('Заказ Оформлен',
            'Войдите в админ панель, что бы просмотреть новый заказ.' ,
            'randylebedenko@gmail.com',
            ['randylebedenko@gmail.com'], fail_silently=False)
        return render(request, 'orders/order/created.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form':form})