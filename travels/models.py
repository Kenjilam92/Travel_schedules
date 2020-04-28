from django.db import models
from login_registration.models import User
from datetime import date, datetime
class PlanManager(models.Manager):
    def plan_validation(self,dataPost):
        errors={}
        for k in dataPost:
            if len(dataPost[k])==0:
                errors[k]='This cannot be empty'
        if not errors:
            a=dataPost['destination']
            b=dataPost['desc']
            c=datetime.strptime(dataPost['date_start'],'%Y-%m-%d')
            d=datetime.strptime(dataPost['date_end'],'%Y-%m-%d')
            e=dataPost['user_id']
            today= datetime.today()
            if c<today:
                errors['date_start']='Please choose a day in the future'
            elif c>d:
                errors['date_end']='Please choose a valid day'                
        return errors

class Plan(models.Model):
    creator= models.ForeignKey(User, related_name='created_plan', on_delete = models.CASCADE)
    destination= models.CharField(max_length=255)
    desc= models.TextField()
    date_start= models.DateField()
    date_end= models.DateField()
    passengers= models.ManyToManyField(User, related_name='joined')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= PlanManager()
    


# Create your models here.
