from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=225, primary_key=True)

    def __str__(self):
        return self.title
