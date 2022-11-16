from django.contrib import admin
from .models import FingerprintProfileModel
from .models import RegisterPersonModel


# Register your models here.
@admin.register(FingerprintProfileModel)
class FingerprintAdminModel(admin.ModelAdmin):
    list_display = ['id', 'username', 'checkinstatus', 'currentdate', 'checkintime', 'exitstatus', 'checkouttime', 'fpid']


@admin.register(RegisterPersonModel)
class RegisterPersonAdminModel(admin.ModelAdmin):
    list_display = ['id', 'personName', 'fpid', 'joiningdatetime']
