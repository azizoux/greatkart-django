from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Saisir votre mot de passe',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmer votre mot de passe',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Entrer Votre Prenom '
        self.fields['last_name'].widget.attrs['placeholder'] = 'Entrer Votre Nom de famille '
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Entrer Votre Numero de téléphone '
        self.fields['email'].widget.attrs['placeholder'] = 'Entrer Votre Email '
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Les mots de passes saisis ne sont pas identitique!"
            )