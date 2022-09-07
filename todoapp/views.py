from django.shortcuts import render,redirect
from .models import TodoList
# Create your views here.
def home(request):
    tasks = TodoList.objects.all()
    
    if request.method == 'POST':
        new_task = request.POST.get('new_task')
        priority = request.POST.get('priority')
        task = TodoList(task_name=new_task,priority=priority)
        task.save()
    return render(request,'index.html',{'tasks':tasks}) 

