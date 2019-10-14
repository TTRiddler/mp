from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from core.models import SEO


class News(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    is_main = models.BooleanField(default=False, verbose_name='Главная новость')
    created_date = models.DateTimeField(default=datetime.today, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/news/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    image_big = ImageSpecField(source='image',
                               processors=[ResizeToFill(930, 523)],
                               format='JPEG',
                               options={'quality': 90})

    image_medium = ImageSpecField(source='image',
                                  processors=[ResizeToFill(690, 388)],
                                  format='JPEG',
                                  options={'quality': 90})

    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(510, 383)],
                                 format='JPEG',
                                 options={'quality': 90})

    image_admin = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 90})
    
    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])

    def image_tag(self):
        return mark_safe('<a href="{0}"><img src="{0}" width="150px"></a>'.format(self.image_admin.url))
    image_tag.short_description = 'Предпросмотр изоражения'
    image_tag.allow_tags = True

    def image_tag_mini(self):
        return mark_safe('<img src="{0}" width="53px">'.format(self.image_admin.url))
    image_tag_mini.short_description = 'Предпросмотр'
    image_tag_mini.allow_tags = True

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('created_date',)

    def __str__(self):
        return self.title
