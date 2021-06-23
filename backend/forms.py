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
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
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
        fields = ['pst_image1','pst_image2','pst_image3','pst_image4','pst_image5','pst_title','pst_description','price','room','bath','toilet','category','sponsored','featured',]
        exclude = ['user', 'm2mthroughfield']
        widget = {
            'pst_image1': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image2': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image3': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image4': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image5': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
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


class FilterForm(forms.ModelForm):
    SALE = "1"
    RENT = "2"
    LEASE = "3"
    CHOOSE = ""

    OFFER_TYPE = [
        (SALE, 'Buy'),
        (RENT, 'Rent'),
        (LEASE, 'lease'),
        (CHOOSE, 'Offer Type')

    ]


    BUNGALOW = "Mansion"
    DUPLEX = "Duplex"
    FLAT = "Flat"
    GLASSHOUSE = "Glasshouse"
    STORY_BUILDING = "Story Building"
    CHOOSE = ""

    PROPERTY_TYPE = [

        (BUNGALOW, 'Mansion'),
        (DUPLEX, 'Duplex'),
        (FLAT, 'Flat'),
        (GLASSHOUSE, 'Duplex'),
        (STORY_BUILDING, 'Block of flat'),
        (CHOOSE, 'Property Type')

    ]

    ONE = "250,000"
    TWO = "150,000,000"
    THREE = "40,000,000"
    FOUR = "1,200,000,000"
    FIVE = "10,200,000"
    SIX = "350,000"
    SEVEN = "13,5000,000"
    EIGHT = "450,000"
    NINE = "500,000"
    TEN = "550,000"
    ONE1 = "600,000"
    TWO2 = "650,000"
    THREE3 = "700,000"
    FOUR4 = "750,000"
    FIVE5 = "800,000"
    SIX6 = "10,000,000"
    SEVEN7 = "40,000,000"
    EIGHT8 = "950,000"
    NINE9 = "1 Million"
    TEN10 = "1.5 Million"
    ONE11 = "2 Million"
    TWO22 = "2.5 Million"
    THREE33 = "3 Million"
    FOUR44 = "3.5 Million"
    FIVE55 = "4 Million"
    SIX66 = "4.5 Million"
    SEVEN77= "5 Million"    
    CHOOSE = ""

    PRICE= [
         (ONE, ' 250,000'),
         (TWO, ' 150,000,000'),
         (THREE, ' 40,000,000'),
         (FOUR, ' 1,200,000,000'),
         (FIVE, ' 10,200,000'),
         (SIX, ' 350,000'),
         (SEVEN, ' 400,000'),
         (EIGHT, ' 450,000'),
         (NINE, ' 500,000'),
         (TEN, ' 550,000'),
         (ONE1, ' 600,000'),
         (TWO2, ' 650,000'),
         (THREE3, ' 700,000'),
         (FOUR4, ' 750,000'),
         (FIVE5, ' 800,000'),
         (SIX6, ' 10,000,000'),
         (SEVEN7, ' 40,000,000'),
         (EIGHT8, ' 950,000'),
         (NINE9, ' 1 Million'),
         (TEN10, ' 1.5 Million'),
         (ONE11, ' 2 Million'),
         (TWO22, ' 2.5 Million'),
         (THREE33, ' 3 Million'),
         (FOUR44, ' 3.5 Million'),
         (FIVE55, ' 4 Million'),
         (SIX66, ' 4.5 Million'),
         (SEVEN77, ' 5 Million'),
         (CHOOSE, 'Price')
    ]

    price = forms.CharField(required=False, label='Price*', widget=forms.Select(choices=PRICE,
        attrs={'class': 'form-control', 'placeholder': 'Price'}))

    pst_title = forms.CharField(required=False, label='Property Type*', widget=forms.Select(choices=PROPERTY_TYPE,
        attrs={'class': 'form-control', 'placeholder': 'Property Type'}))

    category = forms.CharField(required=False, label='Offer Type*', widget=forms.Select(choices=OFFER_TYPE,
        attrs={'class': 'form-control', 'placeholder': 'Offer Type'}))

    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(), empty_label='Please Choose',
    #     widget=forms.Select(attrs={'class': 'form-control'}))
   
    class Meta():
        fields = ['pst_title', 'category', 'price']
        model = PostPage
