from django.shortcuts import render, redirect
from main import models

def index(request):
    context = {

    }

    return render(request, 'front/index.html', context)