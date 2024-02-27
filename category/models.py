from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title
