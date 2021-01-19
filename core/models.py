from django.db import models

# Create your models here.
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