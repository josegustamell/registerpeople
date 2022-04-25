from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-box', 'placeholder': 'Name'}),
            'age': forms.TextInput(attrs={'class': 'form-box', 'placeholder': 'Age'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-box', 'placeholder': 'Birth Date',
                                                 'data-mask': '00/00/0000'}),
            'email': forms.TextInput(attrs={'class': 'form-box', 'placeholder': 'Email'}),
            'nickname': forms.TextInput(attrs={'class': 'form-box', 'placeholder': 'Nickname'}),
            'note': forms.Textarea(attrs={'class': 'form-box', 'placeholder': 'Note'}),
        }
