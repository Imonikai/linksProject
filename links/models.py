from ipaddress import ip_address
from django.db import models
from django.conf import settings

from django.core.validators import URLValidator #URLのバリデータを設定する関数をインポート

# Create your models here.

class Link(models.Model):
    #URLのバリデータを作成、許可はhttp, httpsのみ。
    UrlValidator = URLValidator(
        schemes = ('http', 'https')
    )

    url = models.CharField('リンク', validators=[UrlValidator], max_length=500) #URLfieldにバリデータを設定するとデフォルトのバリデータへの追加での設定になってしまうので、CharFieldを使用する。

    search_word = models.CharField('検索ワード', max_length=200)
    description = models.TextField('コメント', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both')