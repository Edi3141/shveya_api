from rest_framework.viewsets import ModelViewSet
from jobs import serializers
from jobs.models import Job


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer
