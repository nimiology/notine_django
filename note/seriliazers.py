from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from category.models import Category
from category.serializers import CategorySerializer
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())


    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=self.context['request'].user)

    def validate(self, attrs):
        category = attrs.get('category')
        if category.owner != self.context['request'].user:
            raise ValidationError('Category does not belong to the user')
        return super().validate(attrs)

    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(read_only=True)
        return super().to_representation(instance)
