import django.contrib.auth.views as auth_views
from django.urls import path, include
from . import views
app_name = 'user_auth'

urlpatterns = [
    path('', views.top_page, name='top'),
    path('top/', views.top_page, name='top'), # リダイレクト
    path('login/', auth_views.LoginView.as_view(),
    {
        'template_name': 'user_auth/login.html',
    },
    name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
    {
        'template_name': 'user_auth/logout.html'
    },
    name='logout'),
]
