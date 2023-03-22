from rest_framework.viewsets import ModelViewSet
from personal import serializers
from personal.models import Personal


class PersonalViewSet(ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = serializers.PersonalSerializer
