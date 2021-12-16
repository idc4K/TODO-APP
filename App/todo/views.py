from django.shortcuts import render
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
    context = {'q':q,'form':form}
    return render(request, 'todo/index.html', context)
# Create your views here.
