from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('start.urls', namespace='start')),
    path('yatube/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
]
