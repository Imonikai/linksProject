from ipaddress import ip_address
from django.db import models
from django.conf import settings

# Create your models here.

class Link(models.Model):
    url = models.URLField('リンク')
    search_word = models.CharField('検索ワード', max_length=200)
    description = models.TextField('コメント', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both')