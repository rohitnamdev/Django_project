from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples = [
        {'name' : "Abhijit", 'age' : 26},
        {'name' : "Ravi", 'age' : 29},
        {'name' : "Neeraj", 'age' : 16},
        {'name' : "Sandeep", 'age' : 36},
        {'name' : "Rahul", 'age' : 65},
        {'name' : "Gagan", 'age' : 88},
        {'name' : "Ayush", 'age' : 20},
    ]

    return render(request, "home/index.html", context={'peoples':peoples, 'page':'Home'})

def contact(request):
    context = {'page':'contact'}
    return render (request, "home/contact.html", context)
def about(request):
    context = {'page' : 'about'}
    return render (request, "home/about.html", context)
def success_page(reqest):
    context = {'page':'success'}
    return HttpResponse("<h1> This is a success page </h1>", context)