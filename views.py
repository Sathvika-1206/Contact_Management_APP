from django.shortcuts import render
from django.shortcuts import redirect
from .models import Room,Topic
from .forms import RoomForm
# this is the place where we all have our views
# views are basically a request #handler# it takes http request as a argument and sends back the relevant models and template 
# Create your views here.
#url are the ones which trigger the views

# rooms=[
#   {'id':12, "name":"Sathvika"},
#   {'id':2, "name":"Gayathri"},
#   {'id':15, "name":"RSM"},
#   {'id':6, "name":"Shree"},
# ]
def home(request):
  # we can also have context
  rooms=Room.objects.all()
  topic=Topic.objects.all()
  context={"rooms":rooms,"topic":topic}
  return render(request,'base/home.html',context)

def room(request,pk):
  # room=None
  # for i in rooms:
  #   if(i['id']==int(pk)):
  #     room=i
  # give the variable to be inherited=table_name.objects(keyword).function(all(),get() it returns only one value,filter= multiple_values,exclude particular values and create a variable)
  # IT IS A QUERY
  room=Room.objects.get(id=pk)
    #passing only single data instead of the entire case
  context={"room":room}
  return render(request,'base/room.html',context)

def createRoom(request):
  form=RoomForm()
  # if request.method=='POST':
  #   print(request.POST.get('name'))
  if(request.method=='POST'):
    form=RoomForm(request.POST)# to get all the details of the form RoomForm of method POST into the variable form
    if form.is_valid():# it is a function to check whether it is valid form.isvalid(_)
      form.save()# if it is valid then automatically gets saved
      return redirect('home') # we can redirect it by having the name in the path function # you are typically redirecting them
  context={"form":form}
  return render(request,'base/forms.html',context) # to have it extended

def updateRoom(request,pk):
  room=Room.objects.get(id=pk)
  #the room is to get the instance of that object
  form=RoomForm(instance=room)
  if request.method=='POST':
    form=RoomForm(request.POST,instance=room)
    if form.is_valid():
      form.save()
      return redirect('home')
  # in form page u should only render the form model not the room model
  context={'form':form}
  return render(request,'base/forms.html',context)


def deleteRoom(request,pk):
  room=Room.objects.get(id=pk)
  if request.method=="POST":
   room.delete()
   return redirect(home)
  context={"room":room}
  return render(request,'base/delete.html',context)
  