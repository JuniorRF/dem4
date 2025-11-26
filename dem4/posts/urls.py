from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('group/<slug:slug>/', views.group_posts, name='group_page'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('new/', views.new_post, name='new_post'),
    path('detail/<int:pk>/', views.detail_post, name='detail'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('detail/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('detail/<int:pk>/del_comment/<int:id_comment>', views.del_comment, name='del_comment'),

]
