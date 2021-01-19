from django.db import models
from solo.models import SingletonModel

# Create your models here.
class Banner(SingletonModel):
    title = models.CharField('Título', max_length=60)
    
    class Meta:
        verbose_name = 'Banner'

    def __str__(self):
        return "Banner"

class AboutUs(SingletonModel):
    about_us = models.TextField('Sobre nós')
    finance = models.TextField('Finance Outsourcing')
    
    class Meta:
        verbose_name = 'Sobre nós'

    def __str__(self):
        return "Sobre nós"

class Depositions(models.Model):
    name = models.CharField('Nome da pessoa', max_length=50)
    work = models.CharField('Empresa ou ocupação', max_length=50)
    deposition = models.TextField('Texto', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.name 