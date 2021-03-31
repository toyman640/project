from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm



class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email*',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user

class ImageUploadForm(forms.Form):
    profile_photo = forms.ImageField()

    class Meta():
        model = UserProfile


class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
                           widget=forms.Textarea(
                               attrs={'class': 'form-control'}
                           ))
    catch_bot = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field

    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name').capitalize()
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class EditListing(forms.ModelForm):

    class Meta():
        model = PostPage
        exclude = ['date', 'user']

        widget = { 
            'pst_image1': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image2': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image3': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image4': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image5': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'pst_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'toilet': forms.NumberInput(attrs={'class': 'form-control'}),
            'bath': forms.NumberInput(attrs={'class': 'form-control'}),
            'room': forms.NumberInput(attrs={'class': 'form-control'}),
            'cat_id' : forms.Select(attrs={'class': 'form-control'}),
            
            
        }

class NewPost(forms.ModelForm):
    class Meta():
        model = PostPage
        fields = ['pst_image1','pst_image2','pst_image3','pst_image4','pst_image5','pst_title','pst_description','price','room','bath','toilet','category']
        exclude = ['user', 'm2mthroughfield']
        widget = {
            'pst_image1': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image2': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image3': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image4': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image5': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'pst_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'toilet': forms.NumberInput(attrs={'class': 'form-control'}),
            'bath': forms.NumberInput(attrs={'class': 'form-control'}),
            'room': forms.NumberInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
        }
        

class UserEdit(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangeForm(PasswordChangeForm):
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
            return user

