from django.db import models

class UserRegistration(models.Model):
    USER_ID = models.CharField(primary_key=True, max_length=200)
    FIRST_NAME = models.CharField(max_length=200)
    LAST_NAME = models.CharField(max_length=200)
    EMAIL = models.EmailField(max_length=200)
    USERNAME = models.CharField(max_length=200)
    PASSWORD = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)

    def __str__(self):
        return str(self.USER_ID)

    class Meta:
        managed = False
        db_table = 'user_table'


class OrderPlacement(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    retype_password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        managed = False
        db_table = 'order_table'



