from django.urls import path
from . import views
app_name = "server"
urlpatterns = [
    path("",views.page1,name="page1"),
    path("home/",views.home,name="home"),
    path("add/",views.add,name="add"),
    path("end/",views.end,name="end")
]