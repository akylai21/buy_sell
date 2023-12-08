from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        unique=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        help_text='Пример: +996700707070'
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )

    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return f'{self.username}: {self.phone_number}'

    class Meta:
        verbose_name = 'Полбзователь'
        verbose_name_plural = 'Пользователи'
