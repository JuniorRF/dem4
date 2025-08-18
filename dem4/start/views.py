from django.shortcuts import render

def index(request):
    return render(request, 'index.html', )

def ono_tebe_nado(request):
    return render(request, 'ono-tebe-nado.html', )

def posmotri_v_okno(request):
    return render(request, 'posmotri-v-okno.html', )

def slozhno_sosredotochitsya(request):
    return render(request, 'slozhno-sosredotochitsya.html', )

def zakrivayuschiy_teg_f(request):
    return render(request, 'zakrivayuschiy-teg-f.html', )

def mesto(request):
    return render(request, 'mesto.html', )