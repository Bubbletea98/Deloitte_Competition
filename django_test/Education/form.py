from django import forms
from crispy_forms.helper import FormHelper

class NameForm(forms.Form):
    name = forms.CharField(
        label = "真实姓名",
        max_length = 80,
        required = True,
    )

    class Meta :
        fields =['name']