from django.db import models

class notices(models.Model):
    notice = models.CharField(max_length=350)

    def __str__(self):
        return self.notice[:10]
# Create your models here.

class login_detail(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
