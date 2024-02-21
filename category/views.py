from rest_framework.viewsets import ReadOnlyModelViewSet

from category.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = {
        'title': ['icontains'],
    }
    ordering_fields = '__all__'
