from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    phone_number = models.CharField(
        _("phone number"), unique=True, null=False, blank=False, max_length=15
    )
    name = models.CharField(_("Full Name"), null=False, blank=False, max_length=100)
    email = models.EmailField(_("email address"), null=False, unique=True)

    class Meta:
        app_label = "core"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def verify(self):
        self.verified = True
        self.save()
