from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, BaseModelName


class Status(BaseModel, BaseModelName):
    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        ordering = ['-created']
