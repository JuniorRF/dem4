from django.shortcuts import render

def index(request):
    return render(request, 'start/index.html', )

def ono_tebe_nado(request):
    return render(request, 'start/ono-tebe-nado.html', )

def posmotri_v_okno(request):
    return render(request, 'start/posmotri-v-okno.html', )

def slozhno_sosredotochitsya(request):
    return render(request, 'start/slozhno-sosredotochitsya.html', )

def zakrivayuschiy_teg_f(request):
    return render(request, 'start/zakrivayuschiy-teg-f.html', )

def mesto(request):
    return render(request, 'start/mesto.html', )

def web_larek(request):
    return render(request, 'start/web-larek.html', )

def blog_customizer(request):
    return render(request, 'start/blog-customizer.html', )

def stellar_burger(request):
    return render(request, 'start/stellar-burger.html', )