from inspect import classify_class_attrs
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Django의 User를 기반으로 만든 CustomModel라는 클래스를 만들어주세요.



class CustomModel(AbstractBaseUser):
    class Meta:
        db_table = "custom_user"

    address =  models.TextField(max_length=500, blank=True)
    bio =  models.TextField(max_length=500, blank=True)
