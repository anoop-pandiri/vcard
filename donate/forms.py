from django import forms
from .models import Donate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class DonatePaymentForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = "__all__"
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit','Pay', css_class='button white btn-block btn-primary')
        )