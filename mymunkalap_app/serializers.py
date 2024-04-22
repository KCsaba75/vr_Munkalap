
# serializers.py

from rest_framework import serializers
from .models import Megrendelo, Hibatipusok, Munkalap

class MegrendeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Megrendelo
        fields = '__all__'

class HibatipusokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hibatipusok
        fields = '__all__'

class MunkalapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Munkalap
        fields = '__all__'

class MunkalapListSerializer(serializers.ModelSerializer):
    munkalapstatus = serializers.CharField(source='get_munkalapstatus_display')
    uzemenyagszint = serializers.CharField(source='get_uzemenyagszint_display')
    megrendelo_id = MegrendeloSerializer()
    hibatipus_id= HibatipusokSerializer()
    class Meta:
        model = Munkalap
        fields = '__all__'