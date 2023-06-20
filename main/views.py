from django.shortcuts import render, redirect
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

def remove_item(item_id):
        # print(f"ls id:{ls_id}, item id:{item_id}")
        Item.objects.filter(id=item_id).delete()
        # return redirect(to=f"/{ls_id}")


def new_item(response,id):
        ls = ToDoList.objects.get(id=id)

        txt = response.POST.get("new")
        dt = response.POST.get("set_date")

        if len(txt) > 0:
                if dt:
                        ls.item_set.create(text=txt, complete=False, date=dt)
                else:
                        ls.item_set.create(text=txt, complete=False)
        else:
                print("invalid")
        return redirect(to=f"/{id}")
#<!-- {% if td.item_set.filter(complete=False).count>0 %} -->
def index(response, id):
        ls = ToDoList.objects.get(id=id)

        if ls in response.user.todolist.all() and response.method == "POST":
                if response.POST.get("save"):
                        for item in ls.item_set.all():
                                if response.POST.get("c"+str(item.id)) == "clicked":
                                        item.complete = True
                                else:
                                        item.complete = False
                                
                                text = response.POST.get("text" + str(item.id))
                                if text:
                                        item.text = text

                                date = response.POST.get("date" + str(item.id))
                                if date:
                                        item.date = date
                                
                                
                                item.save()
                else:
                        print()
                        Item.objects.filter(id=int(response.POST.get("remove"))).delete()


        return render(response,"main/list.html",{"ls":ls})
        # return render(response,"main/view.html",{})

def home(response):
        lists = ToDoList.objects.filter(user=response.user.id)
        are_incoming = False
        for ls in lists:
                if ls.item_set.filter(complete=False).count() > 0:
                        are_incoming = True
                        break
        
        return render(response,"main/home.html",{"are_incoming":are_incoming})

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