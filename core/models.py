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

class Services(models.Model):
    title = models.CharField('Título', max_length=50)
    text = models.TextField('Texto')
    emoj = models.ImageField(upload_to='services/', verbose_name='Emotion')

    class Meta:
        ordering = ['title']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title

class Strip(models.Model):
    emoj_1 = models.ImageField(upload_to='strip/1/', verbose_name='Primeiro emoticon', null=True, blank=True)
    title_1 = models.CharField('Primeiro título', max_length=12)
    text_1 = models.TextField('Primeiro texto', max_length=100)
    emoj_2 = models.ImageField(upload_to='strip/2/', verbose_name='Segundo emoticon', null=True, blank=True)
    title_2 = models.CharField('Segundo título', max_length=12)
    text_2 = models.TextField('Segundo texto', max_length=100)
    emoj_3 = models.ImageField(upload_to='strip/3/', verbose_name='Terceiro emoticon', null=True, blank=True)
    title_3 = models.CharField('Terceiro título', max_length=12)
    text_3 = models.TextField('Terceiro texto', max_length=100)
    emoj_4 = models.ImageField(upload_to='strip/4/', verbose_name='Quarto emoticon', null=True, blank=True)
    title_4 = models.CharField('Quarto título', max_length=12)
    text_4 = models.TextField('Quarto texto', max_length=100)

    class Meta:
        verbose_name = 'Faixa de informações'

    def __str__(self):
        return "Faixa de informações"

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