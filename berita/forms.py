from django import forms
from berita.models import Artikel
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArtikelForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {

            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
        
            # Use CKEditor widget instead of plain Textarea
            "isi" : CKEditorUploadingWidget(
                config_name='special',
            ),

            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }    