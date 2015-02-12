from django.contrib import admin
from LPARReservation import models

class LPARAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.LPAR, LPARAdmin)
