from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)

def __repr__(self) -> str:
    return f'{self.id}: {self.name}'


class Messages(models.Model):
    message = models.TextField()
    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)   

def __repr__(self) -> str:
    return f'{self.id}: {self.message}'  


class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)

def __repr__(self) -> str:
    return f'{self.id}: {self.comment}'     

