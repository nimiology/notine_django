from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from note.models import Note
from note.seriliazers import NoteSerializer


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class NoteColorsAPI(APIView):
    def get(self, request):
        return {'colors': Note.COLOR_CHOICES}
