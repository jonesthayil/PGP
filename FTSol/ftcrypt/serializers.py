import fields as fields
from rest_framework import serializers
from .models import FTCRYPT


class FTCRYPTSerializer(serializers.ModelSerializer):
    class Meta:
        model = FTCRYPT
        fields = ('postfile',)
