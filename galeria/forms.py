from django import forms

#nome
#legenda
#descricao
#categoria
#foto
#publicada
#data_fotografia
#preco

class CadastroForms(forms.Form):
    nome= forms.CharField(
        label = "Nome:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Venda de Liquidificador"
            }
        )        
    )
    legenda= forms.EmailField(
        label = "Legenda:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Legenda da venda"
            })
    )
    descricao= forms.CharField(
        label = "Descrição:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )    
    categoria= forms.CharField(
        label = "Categoria:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente"
            }
        )
    ) 

