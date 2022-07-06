from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,first_name,last_name,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True

# class User(AbstractUser):
#     # id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
#     phone_number = models.CharField(
#         _("phone number"), unique=True, null=False, blank=False, max_length=15
#     )
#     name = models.CharField(_("Full Name"), null=False, blank=False, max_length=100)
#     email = models.EmailField(_("email address"), null=False, unique=True)

#     class Meta:
#         app_label = "core"
#         verbose_name = _("User")
#         verbose_name_plural = _("Users")

#     def __str__(self):
#         return self.username

#     def verify(self):
#         self.verified = True
#         self.save()
