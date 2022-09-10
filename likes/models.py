from django.db import models
from django.conf import settings

from links.models import Link
# Create your models here.

class Like(models.Model):
    link = models.ForeignKey(Link, verbose_name='リンク', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both')