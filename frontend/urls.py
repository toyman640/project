from django.urls import path
from frontend import views
app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('buy-page', views.buy, name='buy'),
    path('rent-page', views.rent, name='rent'),
    path('contact-page', views.contact, name='contact'),
    # path('login-page', views.login, name='login'),
    path('signup-page', views.signup, name='signup'),
    # path('base-page', views.category, name='category'),
    path('post-cat/<int:category_id>', views.post_from_cat, name='post_from_cat'),
    path('detail-page/<int:abt_id>', views.post_detail, name='post_detail'),
    path('reset-page/', views.resetPage, name='resetPage')
    
]
