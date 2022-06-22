from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NewTaskForm(forms.Form):
    input_task= forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=5)

list_task=[]
def index(request):
    if "task" not in request.session:
        request.session["task"]=[]
    return render(request, "tasks/index.html",{"task":request.session["task"]})

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            get_task=form.cleaned_data["input_task"]
            request.session["task"]+=[get_task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request,"tasks/add.html",{"form":form})
        
    return render(request,"tasks/add.html",{"form":NewTaskForm()})