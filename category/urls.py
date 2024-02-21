from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import CategoryViewSet

app_name = 'category'

router = DefaultRouter()
router.register(r'', CategoryViewSet, basename="category")

urlpatterns = [
    path('', include(router.urls)),
]