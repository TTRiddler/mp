from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from uuid import uuid1


class Employee(models.Model):
    name = models.CharField(max_length=250, verbose_name='ФИО')
    role = models.CharField(max_length=250, verbose_name='Должность')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=20, verbose_name='E-mail')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    is_main = models.BooleanField(default=False, verbose_name='Главный')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/employees/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(128, 128)],
                                     format='JPEG',
                                     options={'quality': 90})

    def image_tag(self):
        return mark_safe('<a href="{0}"><img src="{0}" width="128px"></a>'.format(self.image.url))
    image_tag.short_description = 'Предпросмотр изоражения'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name
