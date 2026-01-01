from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

def notes(request):
    if request.method == "POST":
        if request.POST.get("action") == "delete":
            Students.objects.filter(id=request.POST['id']).delete()
            return render(request, "notes.html",{"notes":Students.objects.all()})
        elif request.POST.get("action") == "edit":
            note = Students.objects.get(id=request.POST['id'])
            return render(request,'add_note.html',{"age":note.age,"name":note.name,"cgpa":note.cgpa,"id":note.id})
        note = Students.objects.get(id=request.POST['id'])
        note.name=request.POST.get("name")
        note.age=request.POST.get("age")
        note.cgpa=request.POST.get("cgpa")
        note.save()
        return redirect("/")
    return render(request, "notes.html",{"notes":Students.objects.all()})
def add_note(request):
    if request.method == "POST":
        Students.objects.create(name=request.POST.get("name"), age=request.POST.get("age"), cgpa=request.POST.get("cgpa"))
        return redirect("/")
    return render(request, "add_note.html")