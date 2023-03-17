from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
# from rating.serializers import ReviewSerializer, ReviewActionSerializer
from .models import Product, Favorites
from . import serializers
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from rest_framework.permissions import BasePermission


class StandartResultPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page'


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'price')
    filterset_fields = ('price', 'title')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    @action(['POST', 'DELETE'], detail=True)
    def favorites(self, request, pk):
        product = self.get_object()
        user = request.user
        if request.method == 'POST':
            if user.favorites.filter(product=product).exists():
                return Response('This product is already in favorites!', status=400)
            Favorites.objects.create(owner=user, product=product)
            return Response('Added to favorites!', status=201)
        else:
            if user.favorites.filter(product=product).exists():
                user.favorites.filter(product=product).delete()
                return Response('Deleted from favorites!', status=204)
            return Response('Product is not found!', status=404)

    # @action(['GET', 'POST'], detail=True)
    # def reviews(self, request, pk):
    #     product = self.get_object()
    #     if request.method == 'GET':
    #         reviews = product.reviews.all()
    #         serializer = ReviewActionSerializer(reviews, many=True).data
    #         return response.Response(serializer, status=200)
    #     else:
    #         if product.reviews.filter(owner=request.user).exists():
    #             return response.Response('You\'ve already reviewed this product!', status=400)
    #         data = request.data
    #         serializer = ReviewActionSerializer(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save(owner=request.user, product=product)
    #         return response.Response(serializer.data, status=201)
    #
    # @action(['DELETE'], detail=True)
    # def review_delete(self, request, pk):
    #     product = self.get_object()
    #     user = request.user
    #     if not product.reviews.filter(owner=user).exists():
    #         return response.Response('You didn\'t reviewed this product!', status=400)
    #     review = product.reviews.get(owner=user)
    #     review.delete()
    #     return response.Response('Successfully deleted!', status=204)
