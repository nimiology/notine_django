from django.urls import include, path
from rest_framework.routers import DefaultRouter

from note.views import NoteViewSet

app_name = 'note'
router = DefaultRouter()
router.register(r'', NoteViewSet, basename="note")
urlpatterns = [
    path('', include(router.urls)),
    path('colors/', NoteViewSet.as_view({'get': 'list_colors'})),
]
