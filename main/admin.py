from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
admin.site.register(ToDoList) #na stronie admina będzie widać todolist
admin.site.register(Item)