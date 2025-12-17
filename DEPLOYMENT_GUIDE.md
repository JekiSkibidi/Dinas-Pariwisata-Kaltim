# Panduan Deploy Django ke Vercel dengan Supabase

## Status Saat Ini ✅

### Data Berhasil Dimigrasikan
- ✅ Database MySQL lokal berhasil di-backup
- ✅ Data dimuat ke Supabase PostgreSQL
- ✅ Users: 2 akun
- ✅ Artikel: 1 artikel
- ✅ Semua perubahan sudah di-push ke GitHub (branch: main)

### Konfigurasi yang Sudah Selesai
- ✅ `.env` - Updated dengan DATABASE_URL Supabase
- ✅ `settings.py` - Dikonfigurasi untuk production (whitenoise, dj-database-url)
- ✅ `wsgi.py` - Ditambahkan alias `app = application`
- ✅ `vercel.json` - File konfigurasi Vercel
- ✅ `build_files.sh` - Script build untuk Vercel
- ✅ `.gitignore` - Updated dengan exclusions lengkap
- ✅ `requirements.txt` - Semua dependencies sudah lengkap
- ✅ Static files - Collected ke folder staticfiles/

## Langkah Deploy ke Vercel

### 1. Login ke Vercel
1. Buka https://vercel.com
2. Login dengan akun GitHub Anda
3. Klik "Add New Project"

### 2. Import Repository
1. Pilih repository: `JekiSkibidi/Dinas-Pariwisata-Kaltim`
2. Branch: `main`
3. Klik "Import"

### 3. Configure Project

#### Framework Preset
- Pilih: **Other** (jangan pilih framework preset)

#### Build and Output Settings
- **Build Command**: `bash build_files.sh`
- **Output Directory**: (kosongkan)
- **Install Command**: `pip install -r requirements.txt`

### 4. Environment Variables
Tambahkan environment variables berikut di Vercel:

```
DATABASE_URL=postgresql://postgres:pororo123@db.icmnovjvjhwesqoudtbh.supabase.co:5432/postgres

SECRET_KEY=django-insecure-ico7bgi=0ao665kv8m$oahtj#1lh-kiv!_ca92s^$r#f)14pbn

DEBUG=False

ALLOWED_HOSTS=.vercel.app,.localhost

ON_SERVER=True
```

**PENTING**: 
- Jangan centang "Automatically expose System Environment Variables"
- Pastikan semua variable dimasukkan dengan benar
- Untuk production, ganti SECRET_KEY dengan key baru yang lebih aman

### 5. Deploy
1. Klik **"Deploy"**
2. Tunggu proses build selesai (sekitar 2-5 menit)
3. Jika berhasil, akan muncul konfetti dan link deployment

### 6. Verifikasi Deployment
Setelah deploy berhasil, test:
1. Buka URL deployment (contoh: `your-project.vercel.app`)
2. Test akses halaman utama
3. Test login ke admin panel: `/admin`
   - Username: admin
   - Password: (password yang Anda buat saat createsuperuser di Supabase)

## Troubleshooting

### Jika Build Gagal

#### Error: "Module not found"
- Pastikan semua dependencies ada di `requirements.txt`
- Run: `pip freeze > requirements.txt` (sudah dilakukan)

#### Error: "Static files not found"
- Pastikan STATIC_ROOT sudah dikonfigurasi di settings.py (sudah selesai)
- Pastikan whitenoise terinstall (sudah selesai)

#### Error: "Database connection failed"
- Periksa DATABASE_URL di environment variables Vercel
- Pastikan format: `postgresql://user:password@host:port/database`

### Jika Halaman Tidak Muncul

#### 404 Not Found
- Periksa `vercel.json` routes configuration
- Pastikan wsgi.py ada alias `app = application`

#### 500 Internal Server Error
1. Check Vercel logs:
   - Buka dashboard Vercel
   - Pilih deployment
   - Klik tab "Functions" atau "Logs"
2. Common issues:
   - DEBUG=True di production (harus False)
   - ALLOWED_HOSTS tidak include domain Vercel
   - Missing environment variables

### Static Files Tidak Muncul
- Pastikan STATICFILES_STORAGE menggunakan whitenoise
- Pastikan whitenoise ada di MIDDLEWARE (posisi kedua)
- Run `python manage.py collectstatic` sebelum deploy

## Maintenance & Update

### Update Kode
```bash
# 1. Buat perubahan di local
# 2. Test di local
python manage.py runserver

# 3. Commit dan push
git add .
git commit -m "Deskripsi perubahan"
git push origin main

# 4. Vercel akan auto-deploy
```

### Update Database
```bash
# Jika ada perubahan model:
python manage.py makemigrations
python manage.py migrate

# Push ke GitHub
git add .
git commit -m "Database migrations"
git push origin main
```

### Backup Database
```bash
# Backup dari Supabase (via Django):
python manage.py dumpdata --natural-foreign --natural-primary --indent 2 -o backup_supabase.json

# Atau dari Supabase Dashboard:
# 1. Login ke https://supabase.com
# 2. Pilih project
# 3. Database > Backups
```

## Informasi Penting

### Database Credentials
- **Type**: PostgreSQL (Supabase)
- **Host**: db.icmnovjvjhwesqoudtbh.supabase.co
- **Port**: 5432
- **Database**: postgres
- **User**: postgres
- **Password**: pororo123

### GitHub Repository
- **URL**: https://github.com/JekiSkibidi/Dinas-Pariwisata-Kaltim
- **Branch**: main

### Local Development
Untuk development lokal, ganti `.env`:
```
# Gunakan MySQL lokal
DB_ENGINE=django.db.backends.mysql
DB_NAME=websitekita
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
```

### Production Settings
Di production (Vercel), gunakan:
```
# Gunakan Supabase
DATABASE_URL=postgresql://postgres:pororo123@db.icmnovjvjhwesqoudtbh.supabase.co:5432/postgres
DEBUG=False
ALLOWED_HOSTS=.vercel.app
```

## Next Steps

1. ✅ Deploy ke Vercel (ikuti langkah 1-5 di atas)
2. ⏳ Test semua fitur di production
3. ⏳ Setup custom domain (optional)
4. ⏳ Enable HTTPS (automatic di Vercel)
5. ⏳ Setup monitoring dan alerts
6. ⏳ Ganti SECRET_KEY dengan key yang lebih aman
7. ⏳ Setup backup schedule untuk database

## Support

Jika ada masalah:
1. Check Vercel deployment logs
2. Check Supabase database logs
3. Test di local environment dulu
4. Pastikan semua environment variables sudah benar

---
**Created**: 2025-01-17
**Last Updated**: 2025-01-17
**Status**: Ready for Deployment 🚀
