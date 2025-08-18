from django.urls import include, path
from . import views

app_name = 'start'

urlpatterns = [
    path('', views.index, name='index'),
    path('ono-tebe-nado', views.ono_tebe_nado, name='ono-tebe-nado'),
    path('posmotri-v-okno', views.posmotri_v_okno, name='posmotri_v_okno'),
    path('slozhno-sosredotochitsya', views.slozhno_sosredotochitsya, name='slozhno-sosredotochitsya'),
    path('zakrivayuschiy-teg-f', views.zakrivayuschiy_teg_f, name='zakrivayuschiy-teg-f'),
    path('mesto', views.mesto, name='mesto'),
]