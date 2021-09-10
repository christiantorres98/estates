from django.db import models
from django.contrib.auth.models import User as UserDjango
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    COMPANY = _("COMPANY")
    USER = _("USER")

    ROLE = (
        (COMPANY, COMPANY),
        (USER, USER),)

    user = models.ForeignKey(UserDjango, on_delete=models.CASCADE)
    document = models.CharField(
        max_length=11,
        verbose_name=_('document'),
        unique=True
    )
    phone = models.CharField(
        max_length=10,
        verbose_name=_("phone"),
        null=True, blank=True
    )
    role = models.CharField(
        max_length=200,
        verbose_name=_("Role"),
        choices=ROLE,
        default=USER
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.get_role_display()}'
