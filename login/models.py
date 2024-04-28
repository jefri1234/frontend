from django.db import models
from django.contrib.auth.models import User


class Notas(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)