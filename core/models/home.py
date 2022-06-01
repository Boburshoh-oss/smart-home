from django.db import models
from uuid import uuid4


class Home(models.Model):
    """
    Home model.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(to='core.User', on_delete=models.CASCADE, related_name='home')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
