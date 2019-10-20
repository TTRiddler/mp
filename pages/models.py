from django.db import models
from uuid import uuid1
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from core.models import SEO, Order


class Page(MPTTModel, SEO, Order):
    ACTION_CHOICES = (
        ('pages', 'Информативная страница'),
        ('home', 'Главная страница'),
        ('albums', 'Фотоотчёты'),
        ('employees', 'Руководство'),
        ('documents', 'Документы'),
        ('news', 'Новости'),
        ('contacts', 'Контакты'),
    )

    title = models.CharField(max_length=250, verbose_name='Название страницы', unique=True)
    body1 = models.TextField(verbose_name='Текст страницы #1', null=True, blank=True)
    body2 = models.TextField(verbose_name='Текст страницы #2', null=True, blank=True)
    body3 = models.TextField(verbose_name='Текст страницы #3', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Показывать в меню')
    action = models.CharField(max_length=32, choices=ACTION_CHOICES, verbose_name='Название модуля')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, related_name='children',
                            verbose_name='Родительская страница', blank=True, null=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    in_footer = models.BooleanField(default=False, verbose_name='Показывать в футере')

    @property
    def subpages(self):
        return Page.objects.filter(parent=self, is_active=True)

    @property
    def firstchild(self):
        return Page.objects.filter(parent=self, is_active=True).first()

    @property
    def subpagescount(self):
        sublist = Page.objects.filter(parent=self, is_active=True)
        return len(sublist)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

mptt.register(Page, )


class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images', verbose_name='Страница')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/pages/{0}/{1}'.format(self.page.slug, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

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


class PageDocument(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='documents', verbose_name='Страница')  
    title = models.TextField(verbose_name='Название документа')
    
    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'documents/pages/{0}/{1}'.format(self.page.slug, filename)

    document = models.FileField(upload_to=get_document_url, verbose_name='Документ')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural ='Документы'


class PageVideo(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='videos', verbose_name='Страница')
    video_link = models.URLField(max_length=250, verbose_name='Ссылка на видео')
    channel_link = models.URLField(max_length=250, verbose_name='Ссылка на канал')

    def __str__(self):
        return self.video_link
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural ='Видео'


class PageQuote(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='quotes', verbose_name='Страница')
    text = models.TextField(verbose_name='Текст цитаты')
    author = models.CharField(max_length=250, verbose_name='Автор цитаты')
    profession = models.CharField(max_length=250, verbose_name='Профессия автора')

    def get_image_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/pages_quote/{1}'.format(self.page.slug, filename)

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