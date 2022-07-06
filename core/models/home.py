from django.db import models
from uuid import uuid4


class Home(models.Model):
    """
    Home model.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(to='core.User', on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
