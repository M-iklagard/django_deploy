from django.shortcuts import render, HttpResponse
from django.views import View

from rest_framework import generics
from . import models
from . import forms
from . import serializers

import requests


# Create your views here.


def main_shop(request):
    category = models.Category.objects.all()
    products = models.Product.objects.all()
    return render(request, context={"category": category, "products": products}, template_name="main.html")


def category(request, chosen_cat):
    products = models.Product.objects.filter(category__name=chosen_cat)
    return render(request, context={"products": products}, template_name="category.html")


def product(request, chosen_product):
    product = models.Product.objects.get(name=chosen_product)
    return render(request, context={"product": product}, template_name="product.html")


class Buy(View):

    def get(self, request, chosen_product):
        """Ця фігня потрібна для відображення форми"""
        form = forms.BueForm(chosen_product)
        return render(request, template_name="buy_form.html", context={"form": form})

    def post(self, request, chosen_product):
        """Ця штука зберігає дані, з цього моменту можна якось надіслати їх у телегу....."""
        form = forms.BueForm(chosen_product, request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            send_order(f"Замовник:\n\n"
                       f"id: {order.id}\n"
                       f"name: {order.name}\n"
                       f"phone: {order.phone}")
            return HttpResponse("Надіслано")

        return render(request, template_name="buy_form.html", context={"form": form})


class AllProducts(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


def send_order(message):
    """Ця фігня відправить повідомлення манагеру"""
    TOKEN = "6361419585:AAFSJwZxG7WOp96PazxiibAt48J5STMmy3A"
    chat_id = 398324319
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, params=params)

