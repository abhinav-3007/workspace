from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from functions import insertRecord, getData, updateListener
import random


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def home(request):
    return render(request, "home.html")


def sender(request):
    data = updateListener("Marks", "Students")
    return JsonResponse(data, safe=False)

def new_user(request):
    alert = "fail"
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if not getData("Marks", "Students", {"email": email}):
            insertRecord("Marks", "Users", {"name": name, "email":email, "password": password})
            alert = "success"
    return JsonResponse(alert, safe=False)


def new_student(request):
    alert = "add"
    if request.method == 'POST':
        name = request.POST['name']
        marks = request.POST['marks']
        roll = request.POST['roll']
        insertRecord("Marks", "Students", {"roll": roll, "name": name, "marks": marks})
    return HttpResponse()
