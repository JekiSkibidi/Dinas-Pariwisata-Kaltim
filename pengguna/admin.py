from django.contrib import admin
from pengguna.models import Biodata, ContactMessage

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ['user','alamat','telpon']
    search_fields = ['user__username']
admin.site.register(Biodata, BiodataAdmin)
admin.site.register(ContactMessage)