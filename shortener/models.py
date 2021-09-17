from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from utils.shortener_utils import get_short_url


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True, blank=True)
    visit_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.original_url} -> {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            size = getattr(settings, 'URL_CHAR_SIZE', 10)
            self.short_url = get_short_url(self, size)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('original_url', 'user')
