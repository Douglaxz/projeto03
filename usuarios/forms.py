from django import forms

class LoginsForms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de Login",
        required=True,
        max_length=100,
    )
    senha_login= forms.CharField(
        label = "Senha de Login",
        required=True,
        max_length=70,
        widget=forms.PasswordInput()
    )
