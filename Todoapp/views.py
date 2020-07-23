from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import Todoform
from .models import Todo
from django.utils import timezone


# Create your views here.
def home(request):
    list = Todo.objects.filter(author=request.user,done=False,lastdate=timezone.now())
    list2 = Todo.objects.filter(author=request.user,done=True,lastdate=timezone.now())
    return render(request,'home.html',{'forms':Todoform(),'list':list,'list2':list2})


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credenial')
            return redirect('login')
    else:
        return render(request,'loginpage.html')


def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        #firstname = request.POST['firstname']
        #lastname = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username is already exists')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email id already exists')
            return redirect('signup')
        else:
            data = User.objects.create_user(username=username,password=password, email=email)
            data.save()
            return redirect('login')
    else:
        return render(request,'signuppage.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def addtodo(request):
    entry1 = Todoform(request.POST)
    if entry1.is_valid():
        user = request.user
        content = request.POST['todo_item']
        lastdate = request.POST['lastdate']
        add = Todo(author=user,todo_item=content,lastdate=lastdate)
        add.save()
        return redirect('home')
    else:
        messages.error(request,'invalid enter')
        return redirect(home)


def delete(request,del_id):
    del_item = Todo.objects.get(id=del_id)
    del_item.delete()
    return redirect('home')

def done(request,done_id):
    done_item=Todo.objects.filter(id=done_id).update(done=True)
    return redirect('home')

