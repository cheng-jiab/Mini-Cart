from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, firstName, lastName, username, email, password=None):
        if not email:
            raise ValueError("Email addrress can not be empty")

        if not username:
            raise ValueError("Username can not be empty")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstName = firstName,
            lastName = lastName,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_superuser funtion will be used when run "createsuperuser" command. Reference: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example
    def create_superuser(self, firstName, lastName, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            firstName = firstName,
            lastName = lastName,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, BaseUserManager):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=50)
    
    # required when create custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    #login using email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  [
        'username',
        'firstName',
        'lastName',
        ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # Mandatory funtions when creat custom user model
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True