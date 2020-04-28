from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def reg_validation(self,dataPost):
        errors={}
        a=dataPost['name']
        b=dataPost['username']
        c=dataPost['password']
        d=dataPost['r_password']
        for k in dataPost:
            if len(dataPost[k])==0:
                errors[k]='This can not be empty'
        if not errors:    
            if len(a)<3:
                errors['name']='This must be more than 3 characters'
            if len(b)<3:
                errors['username']='This must be more than 3 characters'
            elif User.objects.filter(username=b):
                errors['username']='This username was taken. Please choose another name!'
            if len(c)<8:
                errors['password']='This must be more than 8 characters'
            if c!= d:
                errors['r_password']= 'password is not matched'
        return errors    
    def log_validation(self,dataPost):
        errors={}
        a=dataPost['l_username']
        b=dataPost['l_password']
        for k in dataPost:
            if len(dataPost[k])==0:
                errors[k]='This can not be empty'
        if not errors:
            if not User.objects.filter(username=a):
                errors['l_username']='This account have not been registed'
            else:
                selected_user= User.objects.get(username=a).password
                if not  bcrypt.checkpw(b.encode(), selected_user.encode()):
                    errors['l_password']='Password is not correct'
        return errors
class User (models.Model):
    name= models.CharField(max_length=255)
    username= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    objects= UserManager()
    def __repr__(self):
        return self.name
# Create your models here.
