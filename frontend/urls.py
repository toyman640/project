from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('buy-page', views.buy, name='buy'),
    path('rent-page', views.rent, name='rent'),
    path('contact-page', views.contact, name='contact'),
    # path('login-page', views.login, name='login'),
    path('signup-page', views.signup, name='signup'),
    path('temp', views.temp, name='temp'),
    # path('base-page', views.category, name='category'),
    path('post-cat/<int:category_id>', views.post_from_cat, name='post_from_cat'),
    path('detail-page/<int:abt_id>', views.post_detail, name='post_detail'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='frontend/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='frontend/password_reset_sent.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='frontend/password_reset_done.html'), name='password_reset_complete'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('result-page/', views.filter_data, name='filter_data'),

    
]
