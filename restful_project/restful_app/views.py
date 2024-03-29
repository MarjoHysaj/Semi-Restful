from django.shortcuts import render, redirect, HttpResponse
from .models import *
def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "index.html", context)

def new(request):
    return render(request, "new.html")


def create(request):
    print(request.POST)
    show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
    return redirect('/shows/'+str(show.id))

#function:show
#route/shows/id
#method GET

def show(request, id):
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render(request, "show.html", context)

#function:EDIT
#route/shows/id/edit
#method GET

def edit(request, id):
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render(request, "edit.html", context)

#function:update
#route/shows/id/update
#method POST

def update(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect('/shows/'+str(show.id))

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')