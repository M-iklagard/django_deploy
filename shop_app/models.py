from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(blank=False, verbose_name="Категорія", max_length=255)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(blank=False, verbose_name="Назва", max_length=255)
    price = models.FloatField(blank=False, verbose_name="Вартість")
    discription = models.TextField(blank=False, verbose_name="Опис")
    img = models.ImageField(blank=False, verbose_name="Зображення")
    category = models.ForeignKey(Category, blank=False, verbose_name="Категорія", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(blank=False, verbose_name="Замовник", max_length=255)
    phone = models.CharField(blank=False, verbose_name="Номер телефону", max_length=255)
    product = models.ManyToManyField(Product, blank=False, verbose_name="Замовлення")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return self.name
