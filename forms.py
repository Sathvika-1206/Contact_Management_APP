from django.forms import ModelForm
# this way we can import ModelForm from the django.forms
from .models import Room
# we are taking this as a primary table
#in class it is important to name as per the database table name followed by Form
class RoomForm(ModelForm):
  #provide additional information about the model to the django framework
  class Meta:
    #u should specify the model only not the name 
    model=Room
    # it includes all the field of model ROOM
    fields='__all__'

  