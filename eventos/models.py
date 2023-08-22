from django.db import models


class Inscricao(models.Model):

    INTERESSE_OPCOES = (
        ('show', 'Shows de Música'),
        ('futebol', 'Jogos de Futebol'),
        ('outros', 'Outros'),
    )

    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    interesse = models.CharField(verbose_name='Interesse', max_length=50, choices=INTERESSE_OPCOES)
    observacoes = models.TextField(verbose_name='Observações', blank=True)
    data = models.DateTimeField(verbose_name='Data criação', auto_now_add=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ['-data']


class Categoria(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=50)
    criado_em = models.DateTimeField(verbose_name='Data criação', auto_now_add=True)
    modificado_em = models.DateTimeField(verbose_name='Data modificação', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
    

class Evento(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=50)
    categoria = models.ForeignKey(Categoria, models.CASCADE, verbose_name='Categoria')
    data = models.DateField('Data do Evento', null=True, blank=True)
    observacoes = models.TextField('Observações', blank=True)
    destaque = models.BooleanField('Destaque', default=False, blank=True)
    criado_em = models.DateTimeField(verbose_name='Data criação', auto_now_add=True)
    modificado_em = models.DateTimeField(verbose_name='Data modificação', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-criado_em']
