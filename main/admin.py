from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
admin.site.register(ToDoList) #on admin website will be seen todolists and items
admin.site.register(Item)