#first import
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
  name=models.CharField(max_length=300)
  
  def __str__(self):
    return self.name

# we have three tables connected with each other
#class always begin with capital letter
class Room(models.Model):
  host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
  name=models.CharField(max_length=300)
  description=models.TextField(null=True,blank=True)
  updated=models.DateTimeField(auto_now=True)#auto indicates automatic
  created=models.DateTimeField(auto_now_add=True)#once created over
  #be sure it is on the same line and has a return statement it acts as a name for the name field'
  class Meta:
    # ordereing denotes the defaut ordering of the queryset
    # putting - denotes ordering them in the descending order
    #ordering enables you to order them accordingly if - missing then it will order in the ascending order
    ordering=['-updated','-created']

  def __str__(self):
    return self.name
  
class Message(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)# to delete the entire variable
  room=models.ForeignKey(Room,on_delete=models.CASCADE)
  body=models.TextField()# so that the user cannot leave it empty
  updated=models.DateTimeField(auto_now=True)
  created=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.body[0:50]# to return only the first 50 characters
#instance is often dealt with editing or updatinga a particular file
# by stating a instance u are giving a particular room value to the form