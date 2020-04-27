from django import forms


class CheckoutForm(forms.Form):
    state = forms.CharField()
    street_address = forms.CharField()
    apartment_address = forms.CharField(required=False)
    city = forms.CharField()
    zip = forms.CharField()
    phone = forms.CharField()
    payment_option = forms.BooleanField(widget=forms.RadioSelect())