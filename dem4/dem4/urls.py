from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('start.urls', namespace='start')),
    # path('admin/', admin.site.urls),
]
