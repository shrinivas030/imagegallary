from django  import forms
from .models import gallarymodel
class Imageform(forms.ModelForm):
    class Meta:
        model=gallarymodel
        fields = '__all__'
        labels={'pic':' '}