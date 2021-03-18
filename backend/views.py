from django.shortcuts import render,redirect, get_object_or_404
from backend.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        photo_upload_form = ImageUploadForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User Registered')
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('backend:register_form')

        if photo_upload_form.is_valid():
            user = username
            avatar = photo_upload_form.cleaned_data.get("profile_photo")
            new_user_profile = StudentProfile.objects.create(user, avatar)
            
    else:
        register_form = RegisterForm()
        photo_upload_form = ImageUploadForm()


    context = {
        "reg": register_form,
        "photo": photo_upload_form
        }
    return render(request, 'frontend/signup.html', context)

def category_form(request):
    if request.method=='POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category created')
    else:
        category_form = CategoryForm()
    return render(request, 'frontend/signup.html', {'cat':category_form})


def contact(request):
    my_form = FormName()
    return render(request, 'frontend/test.html', {'form_key': my_form})

@login_required(login_url='/dashboard/')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

@login_required(login_url='/backend/login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required(login_url='/dashboard-page/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')