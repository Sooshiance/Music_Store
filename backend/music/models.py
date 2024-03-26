from django.db import models
from django.conf import settings
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title       = models.CharField(max_length = 50, unique=True)
    slug        = models.SlugField(max_length = 100)
    description = models.CharField(max_length = 256, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Music(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length = 50, unique=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug        = models.SlugField(max_length = 100, allow_unicode=True, unique=True)
    description = models.CharField(max_length = 256, blank=True, null=True)
    gener       = models.PositiveSmallIntegerField()
    wallpaper   = models.ImageField(upload_to='music/', default='music.png')
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Music, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} {self.title}'
    
    class Meta:
        managed = True
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'


class Album(models.Model):
    pass
