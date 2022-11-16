from rest_framework import serializers
from .models import FingerprintProfileModel
from .models import RegisterPersonModel


class FingerprintProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintProfileModel
        fields = ['id', 'username', 'checkinstatus', 'currentdate', 'checkintime', 'exitstatus', 'checkouttime', 'fpid']

class RegisterPersonSereializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterPersonModel
        fields = ['id', 'personName', 'fpid', 'joiningdatetime']


