# adresy url do różnych widoków

from django.urls import path
from . import views #importowanie z current dir

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path('view/',views.view, name="create"),
    path("update/<int:id>",views.ItemView.as_view(),name="update")
]