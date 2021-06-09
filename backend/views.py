from django.shortcuts import render,redirect, get_object_or_404
from backend.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from frontend.models import *
from django.http import HttpResponse
from frontend import views 
from django.db.models import Count
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.db import IntegrityError
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode


# Create your views here.
def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            user.profile.first_name = register_form.cleaned_data.get('first_name')
            user.profile.last_name = register_form.cleaned_data.get('last_name')
            user.profile.email = register_form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Galaxy Please Activate Your Account'
            message = render_to_string('backend/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            # messages.success(request, 'Succesfully Registered')
            return redirect('backend:login_view')
    else:
        register_form = RegisterForm() 
        
    return render(request, 'frontend/signup.html', {'reg': register_form})

def activation_sent_view(request):
    return render(request, 'backend/activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Profile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('backend:login_view')
    else:
        return render(request, 'backend/activation_invalid.html')

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
            return redirect('index')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

@login_required(login_url='/backend/login')
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
    posts = PostPage.objects.all().count()
    categories = Category.objects.all().annotate(posts_count=Count('postpage'))
    return render(request, 'backend/dashboard.html', {'post': posts, 'category': categories})

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

@login_required(login_url='/backend/login')
def delete_post(request, listf_id):
    post_record = get_object_or_404(PostPage, id=listf_id)
    post_record.delete()
    return redirect('backend:viewPost')

@login_required(login_url='/backend/login')
def viewUsers(request):
    users = User.objects.all().order_by('last_name')
    post = PostPage.objects.filter(user=request.user)
    return render(request, 'backend/users.html', {'user': users, 'post': post})

@login_required(login_url='/backend/login')
def allPosts(request):
    posts = PostPage.objects.all()
    return render(request, 'backend/allposts.html', {'pst': posts})
