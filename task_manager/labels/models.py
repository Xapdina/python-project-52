from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, BaseModelName


class Label(BaseModel, BaseModelName):
    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
        ordering = ['-created']
