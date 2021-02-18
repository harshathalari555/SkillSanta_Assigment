from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django_extensions.db.fields import RandomCharField
from django.contrib.auth.models import User
from django_mysql.models import ListCharField,ListTextField
from django.db.models import IntegerField


class Batch(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=30)
    code = ListTextField(base_field=RandomCharField(unique=True,include_alpha=True,length=10))
    codes = models.IntegerField()

    def __str__(self):
        return self.batch_name





class Store(models.Model):
    codes = ListTextField(base_field=RandomCharField(unique=True,include_alpha=True,length=10))

    def __str__(self):
        return self.codes



