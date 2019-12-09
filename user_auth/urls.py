import django.contrib.auth.views as auth_views
from django.urls import path, include
from . import views
app_name = 'user_auth'

urlpatterns = [
    path('', views.top_page, name='top'),
    path('top/', views.RecruitmentListView.as_view(), name='top_r'), # リダイレクト
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('recruitment/', views.RecruitCreateView.as_view(), name='recruitment'),
    path('<int:pk>/', views.RecruitmentDatailView.as_view(), name='detail'),
    
]
