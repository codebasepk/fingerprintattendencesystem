from rest_framework import serializers
from .models import FingerprintProfileModel
from .models import RegisterPersonModel


class FingerprintProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintProfileModel
        fields = ['id', 'username', 'checkinstatus', 'currentdate', 'checkintime', 'exitstatus', 'checkouttime', 'fpid']


class RegisterPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterPersonModel
        fields = ['id', 'personName', 'fpid', 'joiningdatetime']

    def update(self, instance, validated_data):
        print(instance.checkinstatus)
        instance.checkinstatus = validated_data.get('checkinstatus', instance.checkinstatus)
        print(instance.checkinstatus)
        instance.fpid = validated_data.get('fpid', instance.fpid)
        instance.currentdate = validated_data.get('currentdate', instance.currentdate)
        instance.save()
        return instance
