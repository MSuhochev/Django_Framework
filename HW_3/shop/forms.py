from django import forms


class FindOrdersForm(forms.Form):
    pk = forms.IntegerField(min_value=1)
    period = forms.ChoiceField(choices=[('week', 'неделя'), ('month', 'месяц'), ('year', 'год')])
