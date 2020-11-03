import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from users.models import Farmer, EquipmentOwner

logger = logging.getLogger('api')


def create_token(user):
    Token.objects.create(user=user)
    logger.info(f'Successfully created authentication token for user {user}')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token_user(sender, instance, created, **kwargs):
    if created:
        create_token(instance)


@receiver(post_save, sender=Farmer)
def create_auth_token_farmer(sender, instance, created, **kwargs):
    if created:
        create_token(instance)


@receiver(post_save, sender=EquipmentOwner)
def create_auth_token_owner(sender, instance, created, **kwargs):
    if created:
        create_token(instance)
