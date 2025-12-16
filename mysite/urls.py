from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from mysite.views import home, about, detail_artikel, contact, submit_contact
from mysite.authentikasi import akun_login, akun_logout, akun_registrasi

from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('submit_contact/', submit_contact, name='submit_contact'),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),

    path('dashboard/', include("berita.urls")),

    path('api/author/list', api_author_list),

    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),

    path('api/artikel/list', api_artikel_list),
    path('api/artikel/add', api_artikel_add),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),
    
    path('authentikasi/login', akun_login, name="akun_login"),
    path('authentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout', akun_logout, name="akun_logout"),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)