from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from .forms import *
def todo(request):
    q = question.objects.all()
    form = questionForm
    context = {'q':q,'form':form}
    return render(request, 'todo/index.html', context)
# Create your views here.
