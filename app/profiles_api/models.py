from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for user profiles'''

    def create_user(self, email:str, name:str, password=None):
        '''Create a new user profile'''
        if(not email):
            raise ValueError("User email is not vaild")
        
        email = self.normalize_email(email)
        new_user = self.model(email=email, name=name)

        new_user.set_password(password)
        new_user.save(using = self._db)

        return new_user

    def create_superuser(self, email, name, password):
        new_user = self.create_user(email, name, password)
        new_user.is_superuser = True
        new_user.is_staff = True

        new_user.save(using=self._db)

        return new_user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False) #is_staff is used to determine if the user is a staff user or not

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_name(self):
        '''Retrive name of user'''
        return self.name
    
    def __str__(self) -> str:
        return self.email