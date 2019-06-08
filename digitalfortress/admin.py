from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Hint)
admin.site.register(models.Round)
admin.site.register(models.Profile)
admin.site.register(models.Solved)
