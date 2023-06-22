from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class ToDoList(models.Model):
    #definiujemy atrybuty
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist",null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) #cascade deleting(delete list->delete all elems)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.text

    @property
    def is_past_due(self):
        return date.today() > self.date

    @property
    def is_close_to_due(self):
        return (date.today() - self.date).days in {0,1}
    
    
