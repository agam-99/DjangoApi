from __future__ import unicode_literals
from django.db import models
import re
class UserManager(models.Manager):
    def validator(self, postData):
        # print(postData.get("name"),flush=True)
        errors = {}

        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if postData['email'] and not re.match(EMAIL_REGEX, postData['email']):
                errors['email1'] = "invalid email"    

        if (User.objects.filter(username=postData['username']).exists()):
                errors['username1'] = "User name already exists"

        if (User.objects.filter(email=postData['email']).exists()):
                errors['email1'] = "email already exists"

        if (postData.get("name").isalpha()) == False:
                errors['name'] = "only alphabets allowed"
        if len(postData.get("name")) < 2:
                errors['name1'] = "name can not be shorter than 2 characters"

        if len(postData.get("username")) < 4:
                errors['username'] = "User name can not be shorter than 4 characters"
        
        if len(postData.get("name")) < 2:
                errors['name'] = "First name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['mobile']) != 10 :
            errors['number'] = "You must enter 10 digit number"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()