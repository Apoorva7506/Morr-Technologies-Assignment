from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email required")
        if not password:
            raise ValueError("Password required")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
   

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ["name","is_staff"]

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

class Contacts(models.Model):
    email=models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    class Meta: 
    
        verbose_name_plural = 'Contacts'