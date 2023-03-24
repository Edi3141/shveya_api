from rest_framework import serializers
from .models import Deals, DealCategory


class DealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DealCategory
        fields = '__all__'


class DealsSerializer(serializers.ModelSerializer):
    deals_category = DealCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Deals
        fields = '__all__'
