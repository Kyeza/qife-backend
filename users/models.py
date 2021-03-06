from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from main.models import BaseModel
from users import utils


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, phone_number email and password.
        """
        now = timezone.now()

        if not username and is_superuser:
            raise ValueError('The given username must be set')
        elif not username and not is_superuser:
            raise ValueError('A valid phone number must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=settings.DEFAULT_APP_PASSWORD, **extra_fields):

        #  ensure phone number is in the format starting with +256
        phone_number = utils.get_international_phone_number_format(phone_number)

        extra_fields.setdefault('phone_number', phone_number)
        return self._create_user(phone_number, None, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('phone_number', None)
        return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractUser, BaseModel):

    class UserTypes(models.TextChoices):
        FARMER = 'FARMER', 'Farmer'
        EQUIP_OWNER = 'EQUIP_OWNER', 'Equipment Owner'

    first_name = models.CharField(verbose_name='first name', max_length=200, null=True, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name='phone number', unique=True, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=UserTypes.choices, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    new_user = models.BooleanField(default=True, null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return str(self.phone_number) if not self.is_superuser else self.email


class FarmerManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(user_type=User.UserTypes.FARMER)


class EquipmentOwnerManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(user_type=User.UserTypes.EQUIP_OWNER)


class Farmer(User):
    objects = FarmerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.FARMER
        return super().save(*args, **kwargs)


class EquipmentOwner(User):
    objects = EquipmentOwnerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.EQUIP_OWNER
        return super().save(*args, **kwargs)
