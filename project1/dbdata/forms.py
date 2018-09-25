from django import forms

from .models import Table1,Table2

class Form(forms.ModelForm):

    class Meta:
        model = Table1
        fields = ('c_date', 'fname', 'email')

