from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Order)


class Admin(admin.ModelAdmin):
    list_filter = ["category"]  # ця фігня повинна саме так і називатись


admin.site.register(models.Product, Admin)
