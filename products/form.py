from django import forms

from .models import Product

# class ProductForms(forms.Form):
#     title=forms.CharField()
class ProductForms(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            'title',
            'content'
        ]

    def clean_content(self):
        data=self.cleaned_data.get('title')
        if len(data)<6:
            raise forms.ValidationError("This is not long enough")
        return data
