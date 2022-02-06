from rest_framework import serializers
from .models import Lender

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = [
            'id', 
            'name', 
            'code', 
            'upfront_commission_rate',
            'trial_commission_rate',
            'active']

class CsvDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = [
            'name', 
            'code', 
            'upfront_commission_rate',
            'trial_commission_rate',
            'active']

class CsvUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()