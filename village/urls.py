from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('home', views.home, name='home'),
  path('home/post/<post_id>', views.post, name='post'),  
  path('new-hood', views.new_hood, name='new-hood'),
  path('home/new-post', views.create_post, name='new-post'),   
  path('join/<hood_id>', views.join_hood, name='join'), 
  path('leave-hood', views.leave_hood, name='leave'),
  path('business', views.business, name='business'),  
  path('schools', views.school, name='schools'), 
  path('hospitals', views.hospital, name='hospitals'), 
  path('myprofile/edit', views.my_profile, name='my_profile'),
  path('myprofile/', views.my_profile, name='my_profile'),
  path('profile/<username>', views.user_profile, name='profile'),
  path('leave', views.leave_hood, name='Leave'),
  path('search/', views.search_hood, name='search_hood'),
  path('search-business/', views.search_business, name='search_business'),
  
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
