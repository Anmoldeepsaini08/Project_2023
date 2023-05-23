from django.db import models

# Create your models here.

class Items(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)



class Users(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_phone = models.IntegerField()
    user_pass = models.CharField(max_length=20)


class Book_table(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    date = models.CharField(max_length=230)
    time = models.CharField(max_length=12,default='')
    people = models.IntegerField(default='')



class Contact_form(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    subject= models.CharField(max_length=20)
    message = models.CharField(max_length=230)

class Sub(models.Model):

    user_email = models.CharField(max_length=20)
    subscribed = models.CharField(max_length=5)
    


