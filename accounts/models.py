from ast import mod
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import ValidationError
from django.utils import timezone
from api.models import Organization, Source


# default manager for the custom user 
class LogmanUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class LogmanUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    organization  = models.ForeignKey(Organization,on_delete=models.PROTECT, null=True)

    objects = LogmanUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class UserSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    source  = models.ForeignKey(Source,on_delete=models.PROTECT)
    user  = models.ForeignKey(LogmanUser,on_delete=models.PROTECT)


        