from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User  

from berita.models import Kategori, Artikel
from berita.forms import ArtikelForm

@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {'title': 'halaman dashboard'}
    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Operator').exists(), login_url='/authentikasi/logout')
def kategori_list(request):
    template_name = "dashboard/snippets/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {'title': 'halaman kategori', 'kategori': kategori}
    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Operator').exists(), login_url='/authentikasi/logout')
def kategori_add(request):
    template_name = "dashboard/snippets/kategori_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        Kategori.objects.create(nama=nama_input)
        return redirect(kategori_list)
    pesan = ""
    context = {'title': 'tambah kategori', 'pesan': pesan}
    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Operator').exists(), login_url='/authentikasi/logout')
def kategori_update(request, id_kategori):
    template_name = "dashboard/snippets/kategori_update.html"
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except Kategori.DoesNotExist:
        return redirect(kategori_list)
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')  
        kategori.nama = nama_input
        kategori.save()
        return redirect(kategori_list)
    context = {'title': 'update kategori', 'kategori': kategori}
    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Operator').exists(), login_url='/authentikasi/logout')
def kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except Kategori.DoesNotExist:
        pass
    return redirect(kategori_list)

@login_required
def artikel_list(request):
    template_name = "dashboard/snippets/artikel_list.html"
    if request.user.groups.filter(name='Operator').exists():
        artikel = Artikel.objects.all()
    else:
        artikel = Artikel.objects.filter(author=request.user)
    context = {'title': 'daftar artikel', 'artikel': artikel}
    return render(request, template_name, context)

@login_required
def artikel_add(request):
    template_name = "dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
    else:
        forms = ArtikelForm()
    context = {'title': 'tambah artikel', 'forms': forms}
    return render(request, template_name, context)

@login_required
def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {'title': artikel.judul, 'artikel': artikel}
    return render(request, template_name, context)

@login_required
def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_artikel)

    if not request.user.groups.filter(name='Operator').exists() and artikel.author != request.user:
        return redirect('/')

    if request.method =="POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)

    forms = ArtikelForm(instance=artikel)
    context = {'title': 'update artikel', 'forms': forms}
    return render(request, template_name, context)

@login_required
def artikel_delete(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
        if not request.user.groups.filter(name='Operator').exists() and artikel.author != request.user:
            return redirect('/')
        artikel.delete()
    except Artikel.DoesNotExist:
        pass
    return redirect(artikel_list)