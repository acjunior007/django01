from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Estoque')

    def __str__(self) -> str:
        return f'{self.nome} ( {self.estoque} )'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobreNome = models.CharField('SobreNome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobreNome}'
