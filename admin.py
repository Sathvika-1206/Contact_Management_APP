from django.contrib import admin
from .models import Room
from .models import Message
from .models import Topic
# Register your models here.
#registering your models into the admin page
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)