from rest_framework import serializers
from .models import Rawpacking


class RawpackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rawpacking
        fields = ['id', 'timestamp', 'serial', 'productionlot', 'productiontype', 'idline', 'idmachine']