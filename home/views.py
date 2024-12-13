from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def home(request):
    if request.method == 'POST'and request.POST.get('title'):
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        Todo.objects.create(title=title,desc= desc)     
    data = Todo.objects.all()    
    return render(request,'home.html',context={'data':data})

def delete(request,id):
    Todo.objects.filter(id = id).delete()
    return redirect('home')

def update(request,id):
    obj = Todo.objects.get(id=id)
    title = obj.title
    desc = obj.desc
    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.desc = request.POST.get('desc')
        obj.date_time = datetime.now()
        obj.save() 
        return redirect('home')
    data = Todo.objects.all()    
    return render(request,'home.html',context={'data':data,'title':title,'desc':desc})    

def search(request):
    search = False
    data = Todo.objects.all()
    title = request.GET.get('search')
    if title:
        search = True
        data = Todo.objects.filter(title__icontains = title) 
    else:
        return redirect('home')    
    return render(request,'home.html',context={'data':data,'search':search})        