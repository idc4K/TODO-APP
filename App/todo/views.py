from django.shortcuts import render
from django.http import HttpResponse

def todo(request):
    return render(request, 'todo/index.html')
# Create your views here.
