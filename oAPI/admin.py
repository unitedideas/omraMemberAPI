from django.contrib import admin
from .models import Rider
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Rider)
class RiderView(ImportExportModelAdmin):
    pass
