from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'loginform/index.html', {})

#def signup(request):
#    form = form(request.POST or None)
#    if form.is_valid():
#        form.save()
#
#    context = {
#    'form' : form
#    }
#    return render(request,'loginform/signup.html', context)

def home(request):
    return render(request, 'loginform/home.html', {})
