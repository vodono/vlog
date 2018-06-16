from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Created at')
    )

    updated = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Updated at')
    )

    class Meta:
        abstract = True
