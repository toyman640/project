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

@login_required(login_url='/backend/login')
def detailView(request, abt_id):
    detail = PostPage.objects.get(id=abt_id)
    return render (request, 'backend/detailview.html', {'det':detail})

@login_required(login_url='/backend/login')
def postEdit(request, blog_id):
    single_blog = get_object_or_404(PostPage, id=blog_id)
    if request.method == 'POST':
        edit_form = EditListing(request.POST, request.FILES, instance=single_blog)
        if edit_form.is_valid():
            blogf = edit_form.save(commit=False)
            blogf.user = request.user
            blogf.save()
            edit_form.save_m2m()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditListing(instance=single_blog)
    return render(request, 'backend/edit_post.html', {'edit_key':edit_form})

@login_required(login_url='/backend/login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required(login_url='/backend/login')
def newPost(request):
    return render(request, 'backend/newpost.html')

@login_required(login_url='/backend/login')
def viewProfile(request):
    profile = UserInfo.objects.filter(user=request.user)
    img =  UserProfile.objects.all()
    return render(request, 'backend/viewprofile.html',{'profile':profile, 'img':img})

@login_required(login_url='/backend/login')
def addProp(request):
    if request.method == 'POST':
        list_form = NewPost(request.POST, request.FILES)
        if list_form.is_valid():
            prop = list_form.save(commit=False)
            prop.user = request.user
            prop.save()
            list_form.save_m2m()
            # messages.success(request, 'Hotel Posted')
            # return redirect('backend:addProp')
            
    else:
        list_form = NewPost()
    return render(request, 'backend/newpost.html', {'prop': list_form})

@login_required(login_url='/backend/login')
def editUser(request):
    if request.method == 'POST':
        edit_form = UserEdit(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = UserEdit(instance=request.user)
    return render(request, 'backend/edit-profile.html', {'edit_key':edit_form})

@login_required(login_url='/backend/login')
def changePwrd(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/reset.html', {'pass_key':pass_form})

def delete_post(request, listf_id):
    post_record = get_object_or_404(PostPage, id=listf_id)
    post_record.delete()
    return redirect('backend:viewPost')
