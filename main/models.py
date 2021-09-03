from django.db import models

# Create your models here.
class UsersManagers(models.Manager):
    
    def basic_validator(self, postData):
        errors={}

        if len(postData['name']) < 4:
            errors["name"] = "el nombre debe tener al menos 4 letras"

        if len(postData['email']) < 4:
            errors["email"] = "el email debe tener al menos 4 letras"

        if len(postData['password']) <6:
            errors["password"] = "la password debe tener al menos 6 letras"

        if postData['password'] != postData['password_confirm']:
            errors["password"] = "ambas contrasenas deben ser iguales"

        return errors


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __repr__(self) -> str:
    return f'{self.id}: {self.name}'


class Messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

def __repr__(self) -> str:
    return f'{self.id}: {self.message}'  


class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __repr__(self) -> str:
    return f'{self.id}: {self.comment}'     

