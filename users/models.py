from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model

from .managers import UserManager
from project.utils import get_file_path

class User(AbstractBaseUser):
    email = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    organization_details = models.TextField(blank=True)
    financial_projections = models.TextField(blank=True)
    organization_charter = models.FileField(blank=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        return self.is_admin
    

    def has_module_perms(self, add_label):
        return True



User = get_user_model()


class Message(models.Model):
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    attachment = models.FileField(upload_to=get_file_path, blank=True)
    seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text