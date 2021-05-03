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


class HududForm(forms.ModelForm):
    class Meta:
        model = Hudud
        fields = ("title",)


class KategoriyaForm(forms.ModelForm):
    class Meta:
        model = SubMuammo
        fields = ("title", "category")
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }


class FoydalanuvchiForm(forms.ModelForm):
    class Meta:
        model = Murojatchi
        fields = ("telegram_id", "username", "fullname", "phone")


class MurojatchiForm(forms.ModelForm):
    class Meta:
        model = Murojatchi
        fields = ("fullname", "status")


class MurojatchiReplyMessageForm(forms.ModelForm):
    class Meta:
        model = Murojatchi
        fields = ("reply_message", "status")
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control px-1 ml-3 mb-2'}),
        }


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['title', 'appointment']
