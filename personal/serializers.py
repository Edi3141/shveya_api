from personal.models import Personal
from rest_framework import serializers


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('user', 'image', 'name', 'email', 'number')
