from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from core.models import SEO
from uuid import uuid1


class News(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок')
    body1 = models.TextField(verbose_name='Текст новости #1', null=True, blank=True)
    body2 = models.TextField(verbose_name='Текст новости #2', null=True, blank=True)
    body3 = models.TextField(verbose_name='Текст новости #3', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    is_main = models.BooleanField(default=False, verbose_name='Главная новость')
    in_main_menu = models.BooleanField(default=False, verbose_name='Отображать в блоке "главное"')
    created_date = models.DateTimeField(default=datetime.today, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/news/{0}'.format(filename)

    image = models.ImageField(max_length=500, upload_to=get_picture_url, verbose_name='Изображение')
    
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
        try:
            image_link = self.image_admin.url
        except:
            image_link = ''
        return mark_safe('<a href="{0}"><img src="{0}" width="150px"></a>'.format(image_link))
    image_tag.short_description = 'Предпросмотр изоражения'
    image_tag.allow_tags = True

    def image_tag_mini(self):
        try:
            image_link = self.image_admin.url
        except:
            image_link = ''
        return mark_safe('<img src="{0}" width="53px">'.format(image_link))
    image_tag_mini.short_description = 'Предпросмотр'
    image_tag_mini.allow_tags = True

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('created_date',)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images', verbose_name='Новость')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/news/{0}/{1}'.format(self.news.slug, filename)

    image = models.ImageField(max_length=500, upload_to=get_picture_url, verbose_name='Изображение')

    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(105, 58)],
                                 format='JPEG',
                                 options={'quality': 90})

    image_standart = ImageSpecField(source='image',
                                    processors=[ResizeToFill(729, 410)],
                                    format='JPEG',
                                    options={'quality': 90})

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class NewsDocument(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='documents', verbose_name='Новость')  
    title = models.TextField(verbose_name='Название документа')
    
    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'documents/news/{0}/{1}'.format(self.news.slug, filename)

    document = models.FileField(max_length=500, upload_to=get_document_url, verbose_name='Документ')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural ='Документы'


class NewsVideo(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='videos', verbose_name='Новость')
    video_link = models.URLField(max_length=250, verbose_name='Ссылка на видео')
    channel_link = models.URLField(max_length=250, verbose_name='Ссылка на канал')

    def __str__(self):
        return self.video_link
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural ='Видео'


class NewsQuote(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='quotes', verbose_name='Новость')
    text = models.TextField(verbose_name='Текст цитаты')
    author = models.CharField(max_length=250, verbose_name='Автор цитаты')
    profession = models.CharField(max_length=250, verbose_name='Профессия автора')

    def get_image_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/news_quote/{1}'.format(self.news.slug, filename)

    image = models.FileField(max_length=500, upload_to=get_image_url, verbose_name='Изображение')

    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(48, 48)],
                                 format='JPEG',
                                 options={'quality': 90})

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural ='Цитаты'