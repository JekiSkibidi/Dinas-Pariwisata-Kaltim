from django import forms
from berita.models import Artikel
from django.contrib.auth.models import User

class ArtikelForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {

            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
        
            # Use plain Textarea - CKEditor will be initialized by CDN script
            "isi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                }),

            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }    