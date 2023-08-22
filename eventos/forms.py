from django import forms

from eventos.models import Inscricao


# class InscricaoForm(forms.Form):

#     INTERESSE_OPCOES = (
#         ('show', 'Shows de Música'),
#         ('futebol', 'Jogos de Futebol'),
#         ('outros', 'Outros'),
#     )

#     nome = forms.CharField(label='Nome', max_length=30)
#     email = forms.EmailField(label='E-mail')
#     interesse = forms.ChoiceField(label='Interesse', choices=INTERESSE_OPCOES)
#     observacoes = forms.CharField(label='Observações', widget=forms.Textarea, required=False)

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'email', 'interesse', 'observacoes']
