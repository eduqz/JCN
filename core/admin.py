from django.contrib import admin
from .models import Depositions, Banner, AboutUs, Services
from solo.admin import SingletonModelAdmin

# Register your models here.
class DepositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'work')

admin.site.register(Depositions, DepositionsAdmin)
admin.site.register(Banner, SingletonModelAdmin)
admin.site.register(AboutUs, SingletonModelAdmin)
admin.site.register(Services)