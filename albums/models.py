from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce import HTMLField
from uuid import uuid1
from core.models import SEO


class Album(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок')
    description = HTMLField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created_date = models.DateField(default=date.today, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/albums/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(510, 287)],
                                     format='JPEG',
                                     options={'quality': 90})
    
    def get_absolute_url(self):
        return reverse('album', args=[self.slug])

    def image_tag(self):
        return mark_safe('<a href="{0}"><img src="{0}" width="200px"></a>'.format(self.image.url))
    image_tag.short_description = 'Предпросмотр изоражения'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Фотоотчёт'
        verbose_name_plural = 'Фотоотчёты'
        ordering = ('created_date',)

    def __str__(self):
        return self.title


class ImageInAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/albums/{0}/{1}'.format(self.album.slug, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(330, 186)],
                                     format='JPEG',
                                     options={'quality': 90})

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return str(self.id)