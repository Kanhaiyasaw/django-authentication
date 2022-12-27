from django.db import models
from django.contrib.auth.models import User

class User_authentication(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , null=True, on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=150)
    city = models.TextField(max_length=150)
    pin_code = models.IntegerField()

    # def __str__(self):
    #     return self.user.username