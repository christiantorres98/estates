from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import User


class Estate(models.Model):
    RURAL = _('RURAL')
    URBAN = _('URBAN')

    TYPE = (
        (RURAL, RURAL),
        (URBAN, URBAN)
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
        blank=True,
        null=True,
        help_text=_('fill in this field if the type of estate is rural')
    )
    address = models.CharField(
        max_length=100,
        verbose_name=_('address'),
        blank=True,
        null=True,
        help_text=_('fill in this field if the type of estate is urban')
    )
    type = models.CharField(
        max_length=20,
        verbose_name=_('type'),
        choices=TYPE,
        default=RURAL
    )
    cadastral_id = models.CharField(
        max_length=20,
        verbose_name=_('catastral itentification'),
        unique=True
    )

    class Meta:
        verbose_name = _("Estate")
        verbose_name_plural = _("Estates")

    def __str__(self):
        return f'{self.cadastral_id}'


class UsersEstates(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )
    estate = models.ForeignKey(
        Estate,
        verbose_name=_('Estate'),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Estates of user')
        verbose_name_plural = _('Estates of users')

    def __str__(self):
        return f'{self.user} - {self.estate}'
