from django.shortcuts import render, redirect
from berita.models import Artikel, Kategori
from django.contrib import messages
from pengguna.models import ContactMessage

def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori == None:
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        print("Bukan ALL")
        try:
            get_kategori = Kategori.objects.get(nama=kategori)
            data_artikel = Artikel.objects.filter(kategori=get_kategori)
            menu_aktif = kategori
        except:
            menu_aktif = "ALL"
            data_artikel = []
    
    data_kategori = Kategori.objects.all()
    context = {
        'title' : 'selamat datang',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori,
        'menu_aktif' : menu_aktif
    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context = {
        'title' : 'selamat datang di halaman about',
        'umur' : 20,
    }
    return render(request, template_name, context)

def contact(request):
    template_name = "halaman/contact.html"
    context = {
        'title' : 'selamat datang di halaman about',
        'umur' : 20,
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name = 'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(slug=slug)
    context = {
        'title': artikel.judul,
        'artikel': artikel
    }
    return render(request, template_name, context)

def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Membuat instance dari model dan menyimpan ke database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        messages.success(request, 'Terima kasih telah menghubungi kami!')
        return redirect('contact')
    else:
        return render(request, 'halaman/contact.html')