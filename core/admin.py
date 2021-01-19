from django.contrib import admin
from .models import Depositions

# Register your models here.
class DepositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'work')

admin.site.register(Depositions, DepositionsAdmin)