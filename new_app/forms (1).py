
from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = [
            "first_name",
            "last_name",
            "crime_type",
            "description",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ismingizni kiriting",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Familiyangizni kiriting",
            }),

            "crime_type": forms.Select(attrs={
                "class": "form-control",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Muammo haqida batafsil yozing",
                "rows": 6,
            }),
        }

    def clean_first_name(self):
        value = self.cleaned_data["first_name"].strip()

        if not value:
            raise forms.ValidationError("Ism kiritish majburiy.")

        return value

    def clean_last_name(self):
        value = self.cleaned_data["last_name"].strip()

        if not value:
            raise forms.ValidationError("Familiya kiritish majburiy.")

        return value
