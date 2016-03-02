import uuid

from django.utils import timezone
from django.db import models
from django.conf import settings


class AbstractBase(models.Model):
    """
    Contains fields that are found in all resources.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   blank=True, null=True,
                                   on_delete=models.PROTECT, related_name='+')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   blank=True, null=True,
                                   on_delete=models.PROTECT, related_name='+')

    class Meta(object):
        abstract = True
