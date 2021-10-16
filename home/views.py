from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def home(request):
    return HttpResponse('Hello,Django')


def details_student(request):
    details = {
        'all_students':[
            {
                'first_name':'Liviu',
                'last_name':'Naframita',
                'hobby':'big',
            },
            {
                'first_name':'George',
                'last_name':'Vasile',
                'hobby':'Ciclism',
            }
        ]
    }
    return render(request,'details_student.html',details)

def details_teacher(request):
    details ={
        'all_teachers':[
            {
                'first_name':'Ion',
                'last_name':'Vasile',
                'class':'Math',

            },
            {
                'first_name': 'Marina',
                'last_name': 'Ion',
                'class': 'Chemistry',
            }
        ]
    }
    return render(request,'details_teacher.html',details)


class HomeTemplateView(TemplateView):
    template_name = 'home.html'