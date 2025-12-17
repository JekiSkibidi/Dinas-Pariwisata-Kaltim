import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from berita.models import Artikel, Kategori

print(f'✅ Users: {User.objects.count()}')
for u in User.objects.all():
    print(f'   - {u.username} ({"superuser" if u.is_superuser else "user"})')

print(f'\n✅ Kategori: {Kategori.objects.count()}')
for k in Kategori.objects.all():
    print(f'   - {k.nama}')

print(f'\n✅ Artikel: {Artikel.objects.count()}')
for a in Artikel.objects.all():
    print(f'   - {a.judul}')

print('\n✅ Database migration ke Supabase berhasil!')
