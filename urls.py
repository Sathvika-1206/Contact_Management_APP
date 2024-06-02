#just to handle all the urls for the base app
#we need to import path function that what triggers the entire url
from django.urls import path
# urls need to have a connection with the view as well
from . import views

# we need to have python list to store all the urls
urlpatterns=[
  #path function have three value
  path('',views.home,name='home'),
  #always end with commas
  #to have dynamic input
  path('room/<str:pk>/',views.room,name='room'),
  path('forms/',views.createRoom,name='createRoom'),
  path('forms/<str:pk>/',views.updateRoom,name='updateRoom'),
  path('delete/<str:pk>/',views.deleteRoom,name='deleteRoom'),
]