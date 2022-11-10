from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Choice


def index(request):
    # return HttpResponse()
    context ={}
    context["set"] = Question.objects.all()
         
    return render(request, "view.html", context)

def index1(request,id):
    
    context ={}
    context["set"] = Choice.objects.filter(question_txt=id)
         
    return render(request, "view1.html", context)

