from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from .models import Profile, Post
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feed, name='feed'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('feed/', views.feed, name='feed'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('profile_list/', views.profile_list, name='profile_list'),
     path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('settings/', views.settings, name='settings'),
    path('like-post/<int:id>', views.like_post, name='like-post'),
    path('shots/<id>', views.shots, name='shots'),
    path('logout/', views.logout, name='logout'),
    path('follow/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)