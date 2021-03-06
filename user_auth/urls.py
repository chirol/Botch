import django.contrib.auth.views as auth_views
from django.urls import path, include
from . import views
app_name = 'user_auth'

urlpatterns = [
    path('top/', views.top_page, name='top'),
    path('', views.RecruitmentListView.as_view(), name='top_r'), # リダイレクト
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('recruitment/', views.RecruitCreateView.as_view(), name='recruitment'),
    path('<int:pk>/', views.RecruitmentDatailView.as_view(), name='detail'),
    path('<int:pk>/update', views.RecruitmentUpdateView.as_view(), name='update'),
    path('dev_top/', views.dev_top, name='dev_top'),
    
]
