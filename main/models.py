from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.
# po edycji tego trzeba zrobi make migrations

#tworzymy model
class ToDoList(models.Model):
    #definiujemy atrybuty
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist",null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    #insacja ToDoList, jesli usuniemy klasę ToDoList, usuwamy tez te linijkę:
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300) #text todo listy 
    complete = models.BooleanField() #czy skoczyliśmy item na todolist
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.text

    @property
    def is_past_due(self):
        return date.today() > self.date

    @property
    def is_close_to_due(self):
        return (date.today() - self.date).days in {0,1}
    
    
