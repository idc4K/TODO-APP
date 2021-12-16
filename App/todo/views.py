from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def todo(request):
    q = question.objects.all()
    context = {'q':q}
    return render(request, 'todo/index.html', context)
# Create your views here.
