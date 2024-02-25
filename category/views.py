from rest_framework.viewsets import ReadOnlyModelViewSet

from category.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    filterset_fields = {
        'title': ['icontains'],
    }
    ordering_fields = '__all__'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
