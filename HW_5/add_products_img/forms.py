from django import forms


class FindOrdersForm(forms.Form):
    pk = forms.IntegerField(min_value=1, label="ID клиента")
    period = forms.ChoiceField(choices=[('week', 'неделя'), ('month', 'месяц'), ('year', 'год')], label="Период")


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    description = forms.CharField(max_length=1000, label="Описание")
    price = forms.DecimalField(max_digits=8, decimal_places=2, label="Цена")
    count = forms.IntegerField(label="Количество")
    image = forms.ImageField(label="Фото товара")
