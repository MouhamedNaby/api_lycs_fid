from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, email,lastName,firstName,phone,adresse, password=None):
        """
        Creates and saves a User with the given email, \and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            lastName= lastName,
            firstName = firstName,
            phone= phone,
            adresse= adresse
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,lastName,firstName,phone,adresse, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
           email=self.normalize_email(email),
            phone=phone,
            password=password,
            firstName=firstName,
            lastName=lastName,
            adresse=adresse
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     blank=True,
    #     related_name='custom_user_permissions'
    # )
    # groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    phone = models.CharField(max_length=40, unique=True )
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=254,unique=True, blank=True, null=True)
    adresse = models.CharField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
   

    objects = MyUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstName','lastName','adresse', 'phone']

    class Meta:
  
        db_table = "api_lycs_fid_user"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.firstName}"