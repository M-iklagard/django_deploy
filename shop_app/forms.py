from django import forms
from . import models


class BueForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"

    # Ця фігня обмежить вибір товару залежно від того на сторінці якого товару ви знаходитесь
    def __init__(self, active_product, *args, **kwargs):
        super(BueForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = models.Product.objects.filter(name=active_product)
