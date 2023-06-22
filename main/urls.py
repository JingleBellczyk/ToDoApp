# adresy url do różnych widoków

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path('view/',views.view, name="create"),
    path("new-item/<int:id>",views.new_item, name="new-item"),
]