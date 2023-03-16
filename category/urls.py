from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, SubcategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
