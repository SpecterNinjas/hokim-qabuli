from django import forms
from panel.models import *


class MahallaForm(forms.ModelForm):
    class Meta:
        model = Mahalla
        fields = ("title", "location", "phone")


class MuammoForm(forms.ModelForm):
    class Meta:
        model = Muammo
        fields = ("title",)


class KategoriyaForm(forms.ModelForm):
    class Meta:
        model = SubMuammo
        fields = ("title", "category")
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }


class MurojatchiForm(forms.ModelForm):
    class Meta:
        model = Murojatchi
        fields = ("fullname", "mahalla", "muammo", "category", "media", "location", "description", "phone", "status")
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(MurojatchiForm, self).__init__(*args, **kwargs)
        field = self.fields.get('status')
        field.choices = field.choices[1:]