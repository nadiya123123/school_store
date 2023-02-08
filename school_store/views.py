from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import FormDataForm,DepartmentForm,CourseForm,PurposeForm,MaterialForm
from .models import Department,Purpose,Course,Material,FormData


def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('school_store:new_page')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('school_store:login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('school_store:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('school_store:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('school_store:register')
    return render(request, "register.html")

def new_page(request):
    return render(request, "new_page.html")

def form(request):
    form = FormDataForm()
    if request.method == 'POST':
        form=FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "order confirmed")
            return redirect('school_store:home')
    return render(request,"form.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect('school_store:home')


def load_course(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})