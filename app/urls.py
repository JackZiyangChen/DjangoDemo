from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("view/<int:id>/", views.view_list, name="view_list"),
    path("home/", views.index, name="index"),
    path("v1/", views.v1, name="view1"),
    path("create/", views.create, name="create")
]