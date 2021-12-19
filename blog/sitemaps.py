from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [
            'pages:home',
            'pages:about',
            'blog:post_list',
            'blog:post_search',
            'blog:post_feed',
            'pages:portfolio',
            'contact_form:contact',
            'login'
            ]

    def location(self, item):
        return reverse(item)
