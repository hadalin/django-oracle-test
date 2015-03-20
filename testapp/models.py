from django.db import models


class TestModel(models.Model):
    text_field = models.TextField(max_length=10000)
