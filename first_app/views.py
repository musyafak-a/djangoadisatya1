from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import student

# Create your views here.
def index(request):
    datas = student.objects.all()
    return HttpResponse(datas)

def create_student(request):
    data = student(name='John', age=20, number_student=12345)
    data.save()
    return HttpResponse("successfully.")

def detail(request, id):
    #  return HttpResponse("show data %s" %id)

    template = loader.get_template('detail.html')
    context = {}

    return HttpResponse(template.render(context, request))