from django.forms import ModelForm
from .models import Sheet


class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = '__all__'
