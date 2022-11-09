from rest_framework import serializers
from .models import FingerprintProfileModel


class FingerprintProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintProfileModel
        fields = ['id', 'username', 'dt', 'status', 'picture', 'ldt', 'lstatus']
