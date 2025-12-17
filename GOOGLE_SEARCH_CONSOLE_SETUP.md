# Panduan Setup Google Search Console untuk dinaspariwisatakaltim.com

## 🎯 Tujuan
Mendaftarkan website dinaspariwisatakaltim.com ke Google Search Console agar website dapat terindeks dan muncul di hasil pencarian Google.

## 📋 Persiapan yang Sudah Selesai

✅ **Sitemap.xml sudah dibuat dan aktif**
- URL Sitemap: https://dinaspariwisatakaltim.com/sitemap.xml
- URL Sitemap: https://www.dinaspariwisatakaltim.com/sitemap.xml
- Sitemap otomatis generate semua artikel dan halaman statis

✅ **Robots.txt sudah dikonfigurasi**
- URL: https://dinaspariwisatakaltim.com/robots.txt
- Sudah termasuk referensi ke sitemap.xml

## 🔧 Langkah 1: Konfigurasi Domain di Vercel

**PENTING**: Sebelum mendaftar ke Google Search Console, pastikan domain sudah terhubung ke Vercel.

### A. Tambah Domain di Vercel Dashboard

1. Buka https://vercel.com/dashboard
2. Pilih project: **Dinas-Pariwisata-Kaltim**
3. Klik tab **Settings** → **Domains**
4. Klik tombol **Add Domain**
5. Masukkan domain: `dinaspariwisatakaltim.com`
6. Klik **Add**
7. Ulangi untuk: `www.dinaspariwisatakaltim.com`

### B. Konfigurasi DNS di Registrar Domain

Vercel akan memberikan instruksi DNS yang harus ditambahkan:

**Untuk domain utama (dinaspariwisatakaltim.com):**
```
Type: A
Name: @
Value: 76.76.21.21
TTL: 3600
```

**Untuk subdomain www:**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600
```

**Langkah setting DNS:**
1. Login ke panel control domain registrar Anda (misalnya: Niagahoster, Namecheap, GoDaddy, dll)
2. Cari menu **DNS Management** atau **DNS Settings**
3. Tambahkan record DNS sesuai instruksi Vercel di atas
4. Simpan perubahan
5. Tunggu propagasi DNS (bisa 1-24 jam)

### C. Verifikasi Domain di Vercel

1. Kembali ke Vercel Dashboard → Settings → Domains
2. Tunggu hingga status domain berubah menjadi **Valid** (ada tanda centang hijau)
3. Pastikan kedua domain (dengan dan tanpa www) sudah Valid

---

## 🔍 Langkah 2: Daftar ke Google Search Console

### A. Verifikasi Domain Utama (dinaspariwisatakaltim.com)

1. **Buka Google Search Console**
   - Kunjungi: https://search.google.com/search-console
   - Login dengan akun Google Anda

2. **Pilih Tipe Properti**
   - Klik tombol **+ Add Property**
   - Pilih **Domain** (bukan URL Prefix)
   - Masukkan: `dinaspariwisatakaltim.com` (tanpa https://)
   - Klik **Continue**

3. **Verifikasi Kepemilikan Domain via DNS**
   
   Google akan memberikan TXT record yang harus ditambahkan ke DNS:
   
   ```
   Type: TXT
   Name: @ (atau kosong)
   Value: google-site-verification=XXXXXXXXXXXXXXXXXXXX
   ```
   
   **Langkah verifikasi:**
   - Copy TXT record yang diberikan Google
   - Buka panel DNS registrar domain Anda
   - Tambahkan TXT record baru sesuai instruksi Google
   - Kembali ke Google Search Console
   - Klik **Verify**
   - Tunggu beberapa menit (maksimal 1 jam)

4. **Alternatif Verifikasi via HTML File** (jika DNS TXT tidak berhasil)
   
   - Pilih metode **HTML file upload**
   - Download file verifikasi (contoh: google123abc.html)
   - Upload file tersebut ke folder `static/` di project Django
   - File harus bisa diakses di: https://dinaspariwisatakaltim.com/google123abc.html
   - Klik **Verify** di Google Search Console

### B. Verifikasi Subdomain www (www.dinaspariwisatakaltim.com)

1. Klik **+ Add Property** lagi
2. Kali ini pilih **URL Prefix**
3. Masukkan: `https://www.dinaspariwisatakaltim.com`
4. Klik **Continue**
5. Gunakan metode verifikasi **HTML tag** atau **HTML file**
6. Ikuti instruksi yang sama seperti di atas

---

## 📤 Langkah 3: Submit Sitemap ke Google Search Console

Setelah domain terverifikasi:

1. **Buka Property Domain di Search Console**
   - Pilih property: dinaspariwisatakaltim.com
   
2. **Submit Sitemap**
   - Klik menu **Sitemaps** di sidebar kiri
   - Di kolom "Add a new sitemap", masukkan: `sitemap.xml`
   - Klik **Submit**
   - Tunggu Google memproses (bisa beberapa jam hingga beberapa hari)

3. **Ulangi untuk subdomain www**
   - Ganti property ke: www.dinaspariwisatakaltim.com
   - Submit sitemap: `sitemap.xml`

---

## ✅ Langkah 4: Monitoring dan Optimasi

### A. Cek Status Indexing

1. Buka menu **Coverage** atau **Pages** di Search Console
2. Lihat berapa halaman yang:
   - Valid (terindeks)
   - Excluded (tidak terindeks)
   - Error (ada masalah)

### B. Request Indexing untuk Halaman Penting

1. Klik menu **URL Inspection** di atas
2. Masukkan URL halaman penting (contoh: homepage, artikel populer)
3. Klik **Test Live URL**
4. Jika valid, klik **Request Indexing**

### C. Monitor Performance

1. Klik menu **Performance**
2. Lihat statistik:
   - Total clicks (klik dari Google)
   - Total impressions (tampilan di hasil pencarian)
   - Average CTR (click-through rate)
   - Average position (posisi rata-rata di hasil pencarian)

---

## 🔔 Langkah 5: Konfigurasi CSRF untuk Domain Custom

Tambahkan domain custom ke settings.py Vercel:

1. Buka Vercel Dashboard → Settings → Environment Variables
2. Edit variable **CSRF_TRUSTED_ORIGINS** atau tambahkan yang baru:
   ```
   Key: CSRF_TRUSTED_ORIGINS
   Value: https://dinaspariwisatakaltim.com,https://www.dinaspariwisatakaltim.com,https://*.vercel.app
   ```
3. Redeploy project agar perubahan berlaku

Atau update di `settings.py`:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://dinas-pariwisata-kaltim.vercel.app',
    'https://dinaspariwisatakaltim.com',
    'https://www.dinaspariwisatakaltim.com',
]
```

---

## 📊 Timeline Ekspektasi

| Tahap | Waktu |
|-------|-------|
| DNS Propagation | 1-24 jam |
| Domain Verifikasi Google | 5-60 menit |
| Sitemap Processing | 1-7 hari |
| Indexing Pertama | 3-14 hari |
| Muncul di Hasil Pencarian | 1-4 minggu |

---

## ⚠️ Troubleshooting

### Domain tidak terverifikasi di Vercel
- Cek apakah DNS record sudah benar
- Tunggu propagasi DNS (gunakan https://dnschecker.org)
- Pastikan tidak ada typo di DNS record

### Google tidak bisa verifikasi domain
- Pastikan TXT record sudah ditambahkan dengan benar
- Tunggu minimal 15 menit setelah tambah TXT record
- Coba refresh cache DNS: `ipconfig /flushdns` (Windows)

### Sitemap tidak terbaca Google
- Cek apakah sitemap bisa diakses langsung di browser
- Pastikan format XML benar (tidak ada error 500)
- Periksa robots.txt tidak memblokir sitemap

### Halaman tidak terindeks
- Cek di URL Inspection apakah ada error
- Pastikan tidak ada tag `noindex` di HTML
- Request indexing manual untuk halaman penting

---

## 📝 Checklist Akhir

Sebelum submit ke Google Search Console, pastikan:

- [ ] Domain sudah terhubung ke Vercel dan Valid
- [ ] Website bisa diakses di https://dinaspariwisatakaltim.com
- [ ] Website bisa diakses di https://www.dinaspariwisatakaltim.com
- [ ] Sitemap.xml bisa diakses (tidak error 404 atau 500)
- [ ] Robots.txt bisa diakses
- [ ] CSRF_TRUSTED_ORIGINS sudah termasuk domain custom
- [ ] Semua artikel memiliki slug yang unik (tidak ada duplicate)
- [ ] File gambar bisa ditampilkan dengan benar

---

## 🎓 Tips Optimasi SEO Lanjutan

1. **Tambahkan Meta Description** di setiap halaman artikel
2. **Gunakan Heading Tags** (H1, H2, H3) dengan struktur yang jelas
3. **Optimasi Gambar**: compress ukuran, gunakan alt text
4. **Internal Linking**: link antar artikel yang relevan
5. **Update Konten Berkala**: artikel baru atau update artikel lama
6. **Mobile-Friendly**: pastikan tampilan mobile responsif
7. **Page Speed**: optimasi loading time website

---

## 🔗 Link Penting

- Google Search Console: https://search.google.com/search-console
- Vercel Dashboard: https://vercel.com/dashboard
- Sitemap Website: https://dinaspariwisatakaltim.com/sitemap.xml
- Robots.txt: https://dinaspariwisatakaltim.com/robots.txt
- DNS Checker: https://dnschecker.org

---

## 📞 Support

Jika ada pertanyaan atau kendala:
1. Cek dokumentasi Google Search Console: https://support.google.com/webmasters
2. Cek dokumentasi Vercel: https://vercel.com/docs
3. Review error di Vercel Logs: Dashboard → Project → Logs

---

**Selamat! Setelah semua langkah ini selesai, website Anda akan mulai muncul di hasil pencarian Google.** 🎉
