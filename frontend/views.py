from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.forms import *
from .filters import PostFilter
from backend.forms import *

# Create your views here.

def index(request):
    sponsored = PostPage.objects.filter(sponsored=True)[:4]
    featured = PostPage.objects.filter(featured=True)[:4]
    post_cat= PostPage.objects.all().order_by('-posted')[:4]
    query_form = FilterForm()
    return render(request, 'frontend/index.html', {'counts':post_cat, 'sponsored':sponsored, 'featured':featured, 'qf':query_form})

def about(request):
    
    return render(request, 'frontend/about.html')

def filter_data(request):
    if request.method == 'GET':
        query_form = FilterForm(request.GET)
        if query_form.is_valid():
            print('Correct')
            price = query_form.cleaned_data.get('price')
            pst_title = query_form.cleaned_data.get('pst_title')
            category = query_form.cleaned_data.get('category')
            post = PostPage.objects.all()
            query = PostPage.objects.filter(category=category,price=price, pst_title=pst_title)
            return render(request, 'frontend/search-result.html', {'q': query})
        else:
            print('Not found')
            return render(request, 'frontend/search-result.html')

def buy(request):
    
    return render(request, 'frontend/buy.html', {'pst':posts})

def rent(request):
    
    return render(request, 'frontend/rent.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name+' '+email+' '+message)
        subject = 'Contact Us Form'
        context = {'name':name, 'email':email, 'message':message }
        html_message =render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <falakoadebayor@gmail.com>'
        send =  mail.send_mail(subject, plain_message, from_email, ['falakoadebayor@gmail.com'], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent successfully')
        else:
            messages.error(request, 'Email not sent')
    return render(request, 'frontend/contact.html')

# def login(request):
    
#     return render(request, 'frontend/login.html')

def signup(request):
    
    return render(request, 'frontend/signup.html')

def post(request):
     return render(request, 'frontend/rent.html' )

def post_from_cat(request, category_id):
    count_post = PostPage.objects.filter(category__id=category_id).order_by('-posted')
    paginated_filter = Paginator(count_post, 6)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    try:
        get_cat_name = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    # get_cat_name = Category.objects.get(id=category_id)
    post_cat= PostPage.objects.filter(category__id=category_id).order_by('-posted')
    context = {'person_page_obj': count_post, 'posts': post_cat, 'counts': count_post, 'cat': get_cat_name}
    context['person_page_obj'] = person_page_obj
    return render(request, 'frontend/post.html', context)

def post_detail(request, abt_id):
    post = PostPage.objects.get(id=abt_id)
    return render(request, 'frontend/property-details.html', {'post':post})

def resetPage(request):
    return render(request, 'frontend/resetpage.html')

def temp(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # messages.success(request, 'Succesfully Registered')
            return redirect('backend:login_view')
    else:
        register_form = RegisterForm() 
    return render(request, 'frontend/front_temp.html',  {'reg': register_form})

# def searchPage(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         post = PostPage.objects.filter(pst_title__contains=searched)
#         return render(request, 'frontend/search-result.html', {'searched': searched, 'pst':post})
#     else:

#         return render(request, 'frontend/search-result.html')
    