
#this is the collection of urls
#here present all the routing urls 
from django.contrib import admin
from django.urls import path
from django.urls import include #include is used to get connection from other apps
# remember to import by having the syntax from django.http<that is the http> import HttpResponse

#this url is for the full project
#url are the ones which trigger the views


urlpatterns = [
    path('admin/', admin.site.urls),
    #we need to specify a path i.e the core path ""
    #ideat include base.urls . not the / that is only for templates include base.urls
    path('',include('base.urls')),
    #u need to give it another ' '
    
]
