from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, UpdateAPIView

from category.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet, CreateAPIView, UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = {
        'title': ['icontains'],
    }
    ordering_fields = '__all__'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)