from django.shortcuts import render
import random

def project(request):
    lucky_number = random.randint(1,100)
    context = {"lucky_number" : lucky_number}                               #{a,b}, a -> name of the function that will be called by the django command written in the html code. b is the variable passed here in the views.  
    return render(request, "project/project.html", context)
# Create your views here.
