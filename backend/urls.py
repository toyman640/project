from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('login', views.login_view, name='login_view'),
    path('register-form/', views.register_form, name='register_form'),
    path('category/', views.category_form, name='category_form'),
    path('view_contact/', views.contact, name='contact'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('view-post/', views.viewPost, name='viewPost'),
    path('dashboard/', views.dashboard, name='dashboard',),
    path('deatilview-page/', views.detailView, name='detailView'),
    path('newpost-page/', views.newPost, name='newPost'),
]