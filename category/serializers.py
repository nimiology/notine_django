from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['owner']

    def validate(self, attrs):
        title = attrs.get('title')
        owner = attrs.get('owner')
        try:
            Category.objects.get(title=title, owner=owner)
            raise ValidationError('Category already exists')
        except Category.DoesNotExist:
            return super().validate(attrs)