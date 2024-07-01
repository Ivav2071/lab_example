from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    product_name = forms.CharField(label='Наименование товара')  # Создаем новое поле product_name типа CharField
    full_name = forms.CharField(label='Ваше полное имя:')
    email = forms.CharField(label='Введите ваш @mail:')
    address = forms.CharField(label='Адрес получения :')

    phone_number = forms.CharField(label='Номер телефона')

    class Meta:
        model = Order
        fields = ['product_name', 'full_name', 'email', 'address', 'phone_number']