from django.db import models

# Create your models here.

class Movie(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    id_ator = models.ManyToManyField("Ator", verbose_name="Ator")
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ("nome",)
    
    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    gender = models.CharField(max_length=50, verbose_name="Genero")
    idade = models.PositiveBigIntegerField(default=0, verbose_name="Idade")
    created_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
        ordering = ("nome",)
    
    def __str__(self):
        return self.nome