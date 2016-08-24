from django import forms
from django.conf import settings
from .models import Codification


class FormCodification(forms.ModelForm):

    def save(self, commit=True):
        codification = super(FormCodification, self).save(commit=False)
        if commit:
            codification.save()
        return codification

    class Meta:
        model = Codification
        fields = ["description", "image"]
