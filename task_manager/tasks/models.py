from django.contrib.auth import get_user_model
from django.db import models
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, BaseModelName


class Task(BaseModel, BaseModelName):
    description = models.TextField(_('description'), blank=True)

    creator = models.ForeignKey(get_user_model(),
                                on_delete=models.PROTECT,
                                verbose_name=_('creator'),
                                related_name='create_tasks'
                                )

    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.PROTECT,
                                 verbose_name=_('executor'),
                                 related_name='executor_tasks',
                                 blank=True,
                                 null=True
                                 )

    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,  # сносим 1 статус
                               verbose_name=_('status'),
                               related_name='tasks'
                               )

    labels = models.ManyToManyField(Label,
                                    related_name='tasks',
                                    verbose_name=_('labels'),
                                    blank=True,
                                    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
