from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users', views.user_view, name='users'),
    path('pages', views.page_view, name='pages'),
    path('posts', views.post_view, name='posts'),
    path('songs', views.song_view, name='songs'),
]
