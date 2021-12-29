from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

from .forms import *
def todo(request):
    q = question.objects.all()
    form = questionForm
   
   #Creation d'une question 
    if request.method == 'POST':
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'q':q,'form':form}
    return render(request, 'todo/index.html', context)

def modifier(request, pk):
    c = question.objects.get(id=pk)

    form = questionForm(instance=c)
   
    if request.method == 'POST':
        form = questionForm(request.POST, instance=c)

        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

   
    return render(request, 'todo/update.html',context)
# Create your views here.

def supprimer(request,pk):
    item = question.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todo/delete.html', context)

