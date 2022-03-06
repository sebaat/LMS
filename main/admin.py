from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Account)
admin.site.register(models.Sanction)
admin.site.register(models.Persson)
admin.site.register(models.Inscription)
admin.site.register(models.Exemplaire)
admin.site.register(models.Book)
admin.site.register(models.Order)
admin.site.register(models.Riter)
