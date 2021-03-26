from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def index(request):
    
    return render(request, 'frontend/index.html')

def about(request):
    
    return render(request, 'frontend/about.html')

def buy(request):
    
    return render(request, 'frontend/buy.html', {'pst':posts})

def rent(request):
    
    return render(request, 'frontend/rent.html')

def contact(request):
    
    return render(request, 'frontend/contact.html')

# def login(request):
    
#     return render(request, 'frontend/login.html')

def signup(request):
    
    return render(request, 'frontend/signup.html')

def post(request):
     return render(request, 'frontend/rent.html' )

def post_from_cat(request, category_id):
    count_post = PostPage.objects.filter(category__id=category_id).count()
    try:
        get_cat_name = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    # get_cat_name = Category.objects.get(id=category_id)
    post_cat= PostPage.objects.filter(category__id=category_id)
    context = {'posts': post_cat, 'counts': count_post, 'cat': get_cat_name}
    return render(request, 'frontend/post.html', context)

def post_detail(request, abt_id):
    post = PostPage.objects.get(id=abt_id)
    return render(request, 'frontend/property-details.html', {'post':post})
    