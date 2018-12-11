from django.contrib import admin
from .models import MemberData
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(MemberData)
class MemberDataView(ImportExportModelAdmin):
    pass
