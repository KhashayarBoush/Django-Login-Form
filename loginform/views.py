from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'loginform/index.html', {})
