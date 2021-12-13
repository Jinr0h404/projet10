from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("veuillez entrer un email")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    """this class is for the django orm, it gives the parameters for the
            creation of the table of the same name in the psql database."""
    username = models.CharField(max_length=200, null=False, blank=False, verbose_name="Nom")
    email = models.EmailField(max_length=45, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(selfself, app_label):
        return True

    def __str__(self):
        return f'{self.username} | {self.email}'
