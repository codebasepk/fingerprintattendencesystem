from django.contrib import admin
from .models import FingerprintProfileModel


# Register your models here.
@admin.register(FingerprintProfileModel)
class FingerprintAdminModel(admin.ModelAdmin):
    list_display = ['id', 'username', 'dt', 'status', 'picture', 'ldt', 'lstatus']
