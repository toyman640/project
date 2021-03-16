from django.shortcuts import render,redirect
from . import forms
from backend.forms import RegisterForm
from backend.forms import CategoryForm
from backend.forms import FormName
from backend.forms import *

# Create your views here.
def register_form(request):
    if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'User Registered')
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
