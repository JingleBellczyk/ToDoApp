from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from datetime import datetime
# Create your views here. tworzenie widoków
from .serializers import ItemSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import DjangoModelPermissions

# class ItemView(RetrieveAPIView):
#         http_method_names = ["get","patch"]
#         permission_classes = [DjangoModelPermissions]
#         serializer_class = ItemSerializer

#         lookup_field = "id"
                
#         def get_queryset(self):
#                 print("tutaj")
#                 return Item.objects.all()



def index(response, id):
        ls = ToDoList.objects.get(id=id)

        if ls in response.user.todolist.all():
                if response.method == "POST":
                        print(response.POST)
                        if response.POST.get("save"):
                                for item in ls.item_set.all():
                                        if response.POST.get("c"+str(item.id)) == "clicked":
                                                item.complete = True
                                        else:
                                                item.complete = False
                                        
                                        text = response.POST.get("text" + str(item.id))
                                        print(text)
                                        if text:
                                                item.text = text

                                        date = response.POST.get("date" + str(item.id))
                                        if date:
                                                item.date = date
  
                                        item.save()
                                
                        elif response.POST.get("newItem"):
                                txt = response.POST.get("new")
                                dt = response.POST.get("set_date")
                                if dt:
                                        if len(txt) > 0:
                                                ls.item_set.create(text=txt, complete=False,date=dt)
                                        else:
                                                print("invalid")
                                else:
                                        if len(txt) > 0:
                                                ls.item_set.create(text=txt, complete=False)
                                        else:
                                                print("invalid")

                # item = ls.item_set.get(id=1)
                return render(response,"main/list.html",{"ls":ls})
        return render(response,"main/view.html",{})

        # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

def home(response):
        return render(response,"main/home.html",{})

def create(response):
        if response.method == "POST":
                form = CreateNewList(response.POST)
                if form.is_valid():
                       n = form.cleaned_data["name"]
                       t = ToDoList(name=n)
                       t.save()
                       response.user.todolist.add(t)

                return HttpResponseRedirect("/%i" %t.id) #przekierowanie do strony z id tej listy
        else:
                form = CreateNewList()
        return render(response,"main/create.html",{"form":form})
      

def view(response):
        return render(response,"main/view.html",{})

# def v1(response):
#     return HttpResponse("<h1>View 1</h1>")