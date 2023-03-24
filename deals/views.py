from rest_framework import permissions
from rest_framework import viewsets
from .models import Deals, DealCategory
from .serializers import DealsSerializer, DealCategorySerializer


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer


class DealCategoryViewSet(viewsets.ModelViewSet):
    queryset = DealCategory.objects.all()
    serializer_class = DealCategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
