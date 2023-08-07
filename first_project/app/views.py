import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from app.models import Homework


def home_view(request):
    index_list = Homework.objects.all()
    template_name = 'app/list.html'
    return render(request, template_name, {'index_list': index_list})


def time_view(request):
    time = datetime.datetime.now().time()
    template_name = 'app/current_time.html'
    return render(request, template_name, {'time': time})


def workdir_view(request):
    dir = os.listdir(path='.')
    template_name = 'app/workdir.html'
    return render(request, template_name, {'directory': dir})
