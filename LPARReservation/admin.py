from django.contrib import admin
from LPARReservation import models

class LPARAdmin(admin.ModelAdmin):
    pass

class ServerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.LPAR, LPARAdmin)
admin.site.register(models.Server, ServerAdmin)
