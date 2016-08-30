from django import forms
from django.conf import settings
from .models import Codification, Segmentation


class FormCodification(forms.ModelForm):

    def save(self, commit=True):
        codification = super(FormCodification, self).save(commit=False)
        if commit:
            codification.save()
        return codification

    class Meta:
        model = Codification
        fields = ["image"]


class FormSegmentation(forms.ModelForm):

    def save(self, commit=True):
        segmentation = super(FormSegmentation, self).save(commit=False)
        if commit:
            segmentation.save()
        return segmentation

    class Meta:
        model = Segmentation
        fields = ["image", "concept"]
