from rest_framework import serializers

from category.serializers import CategorySerializer
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(read_only=True)
        return super().to_representation(instance)