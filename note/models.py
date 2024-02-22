import random

from django.contrib.auth import get_user_model
from django.db import models

from category.models import Category

COLOR_CHOICES = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Orange', 'Orange'),
    ('Purple', 'Purple'),
    ('Teal', 'Teal'),
    ('Pink', 'Pink'),
    ('Cyan', 'Cyan'),
    ('Amber', 'Amber'),
    ('Indigo', 'Indigo'),
    ('Lime', 'Lime'),
    ('Brown', 'Brown'),
    ('Deep Purple', 'Deep Purple'),
    ('Light Blue', 'Light Blue'),
    ('Light Green', 'Light Green'),
    ('Deep Orange', 'Deep Orange'),
    ('Grey', 'Grey'),
    ('Blue Grey', 'Blue Grey'),
    ('White', 'White'),
    ('Deep Orange Accent', 'Deep Orange Accent'),
    ('Deep Purple Accent', 'Deep Purple Accent'),
    ('Green Accent', 'Green Accent'),
    ('Amber Accent', 'Amber Accent'),
    ('Blue Accent', 'Blue Accent'),
    ('Cyan Accent', 'Cyan Accent'),
    ('Orange Accent', 'Orange Accent'),
    ('Indigo Accent', 'Indigo Accent'),
    ('Pink Accent', 'Pink Accent'),
    ('Red Accent', 'Red Accent'),
]


def random_color():
    return COLOR_CHOICES[random.randint(0, len(COLOR_CHOICES) - 1)]


class Note(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=100, default=random_color, choices=COLOR_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
