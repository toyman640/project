from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register-form/', views.register_form, name='register_form'),
    path('category/', views.category_form, name='category_form'),
    path('view_contact/', views.contact, name='contact'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('view-post/', views.viewPost, name='viewPost'),
    path('dashboard/', views.dashboard, name='dashboard',),
    path('detailview-page/<int:abt_id>', views.detailView, name='detailView'),
    path('newpost-page/', views.addProp, name='addProp'),
    path('viewprofile-page/', views.viewProfile, name='viewProfile'),
    path('editpost-page/<int:blog_id>', views.postEdit, name='postEdit'),
    path('edit-profile-page/', views.editUser, name='editUser'),
    path('reset/', views.changePwrd, name='changePwrd'),
    path('delete-property/<int:listf_id>', views.delete_post, name='delete_post'),
    path('userlist-page/', views.viewUsers, name='viewUsers'),
]