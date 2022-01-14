from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList

# Create your views here.


def index(response):
    return HttpResponse("<h1>hello world</h1>")


def view_list(response, id):
    list = ToDoList.objects.get(id=id)
    if response.method=='POST':
        if response.POST.get("save"):
            for item in list.item_set.all():
                item.complete = response.POST.get("check_"+str(item.id)) == "clicked"
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 0:
                list.item_set.create(text=txt, complete=False)


    return render(response, "main/list.html", {"list": list})


def v1(response):
    return HttpResponse("this leads to v1 page")


def home(response):
    return render(response, "main/home.html", {}) # dictionary represents the variable to pass in


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect("/view/%i/" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})