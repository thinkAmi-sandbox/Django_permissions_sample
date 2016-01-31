from django.db import models

class Article(models.Model):
    public_content = models.CharField('public', max_length=255)
    private_content = models.CharField('private', max_length=255)
    permission_content = models.CharField('private', max_length=255)
    
    # Metaオプションにて、パーミッション設定
    class Meta:
        permissions = (
            ("can_view", "Can see content"),
        )
