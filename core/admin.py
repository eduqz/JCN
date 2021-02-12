from django.contrib import admin
from .models import Depositions, Banner, AboutUs, Services, Strip
from solo.admin import SingletonModelAdmin

# Register your models here.
class DepositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'work')

class StripAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >=1:
            return False
        else:
            return True

admin.site.register(Depositions, DepositionsAdmin)
admin.site.register(Banner, SingletonModelAdmin)
admin.site.register(AboutUs, SingletonModelAdmin)
admin.site.register(Services)
admin.site.register(Strip, StripAdmin)