from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class TaskDeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'form'
    fields = ('name','priorit','date')
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class TaskDetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'

# Create your views here.
def todo_fun(request):
    task1=Task.objects.all()

    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,priorit=priority,date=date)
        task.save()

    return render(request,'home.html',{'task':task1})

# def details(request):
#     return render(request,'details.html',)

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"edit.html",{'task':task,'form':form})