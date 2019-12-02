from django import forms
from django.db.models.fields import IntegerField

from .models import Company


class CompanyFormOld(forms.Form):
    name = forms.CharField(required=True)
    tax_number = forms.IntegerField(required=True, label="Tax no.", initial=0)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = [
            'created_at',
            'last_modified_at',
            'created_by',
            'last_modified_by'
        ]
