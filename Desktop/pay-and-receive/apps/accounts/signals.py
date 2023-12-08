from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django_rest_passwordreset.signals import reset_password_token_created

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse

User = get_user_model

@receiver(post_save, sender=User)
def send_notificatoin_user(sender, instance, created, **kwargs):
    if created:
        subject = f'Уводомление о регистрации.'
        message = f'''Приветствуем {instance.username}.
Вы успешно зарегистрированы!
'''
        from_emil = settings.ENAIL_HOST_USER
        to_email = instance.email
        send_mail(subject, message, from_emil, [to_email] )

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    subject = f'Восстановление пароля'
    message = f'''Приветствуем {reset_password_token.user.username}.
    Всатвьте ниже сгенерованный токен!:
            {reset_password_token.key}
    '''
    from_emil = settings.EMAIL_HOST_USER
    to_email = reset_password_token.user.email
    send_mail(subject, message, from_emil, [to_email])
