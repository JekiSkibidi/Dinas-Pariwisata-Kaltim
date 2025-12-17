from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from berita.models import Artikel, Kategori


class StaticViewSitemap(Sitemap):
    """Sitemap untuk halaman statis"""
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)


class ArtikelSitemap(Sitemap):
    """Sitemap untuk artikel/berita"""
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Artikel.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('detail_artikel', args=[obj.slug])
