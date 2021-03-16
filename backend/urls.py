from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('register-form/', views.register_form, name='register_form'),
    path('category/', views.category_form, name='category_form'),
    path('view_contact/', views.contact, name='contact'),
]