from django.shortcuts import render,redirect, get_object_or_404
from backend.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from frontend.models import *

# Create your views here.
def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # messages.success(request, 'Succesfully Registered')
            return redirect('backend:login_view')
    else:
        register_form = RegisterForm() 
        
    return render(request, 'frontend/signup.html', {'reg': register_form})

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

# @login_required(login_url='/backend/')
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

@login_required(login_url='/backend/login')
def viewPost(request):
    prop = PostPage.objects.filter(user=request.user)
    cat = Category.objects.all()
    return render(request, 'backend/viewposts.html', {'view':prop, 'cat':cat})

def detailView(request, abt_id):
    detail = PostPage.objects.get(id=abt_id)
    return render (request, 'backend/detailview.html', {'det':detail})

def postEdit(request, blog_id):
    single_blog = get_object_or_404(PostPage, id=blog_id)
    if request.method == 'POST':
        edit_form = EditListing(request.POST, request.FILES, instance=single_blog)
        if edit_form.is_valid():
            blogf = edit_form.save(commit=False)
            blogf.user = request.user
            blogf.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditListing(instance=single_blog)
    return render(request, 'backend/edit_post.html', {'edit_key':edit_form})


def dashboard(request):
    return render(request, 'backend/dashboard.html')

def newPost(request):
    return render(request, 'backend/newpost.html')

def viewProfile(request):
    profile = UserInfo.objects.filter(user=request.user)
    img =  UserProfile.objects.all()
    return render(request, 'backend/viewprofile.html',{'profile':profile, 'img':img})

def addProp(request):
    if request.method == 'POST':
        list_form = NewPost(request.POST, request.FILES)
        if list_form.is_valid():
            prop = list_form.save(commit=False)
            prop.user = request.user
            prop.save()
            # messages.success(request, 'Hotel Posted')
            
    else:
        list_form = NewPost()
    return render(request, 'backend/newpost.html', {'prop': list_form})