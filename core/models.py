from django.db import models
from uuid import uuid1
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class SEO(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        abstract = True


class Order(models.Model):
    position = models.PositiveIntegerField(blank=True, verbose_name='Позиция')

    def save(self, *args, **kwargs):
        if self.position is None:
            try:
                last = self.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Order, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)


class MainTitle(models.Model):
    title = models.CharField(max_length=250, verbose_name='Главный заголовок')

    class Meta:
        verbose_name = 'Главный заголовок'
        verbose_name_plural = 'Главный заголовок'

    def __str__(self):
        return self.title


class Goal(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.text


class Pros(models.Model):
    BG_CHOICES = (
        ('primary', 'Красный'),
        ('secondary', 'Синий'),
    )

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    bg_color = models.CharField(max_length=250 ,choices=BG_CHOICES, verbose_name='Цвет фона')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/pros/{0}'.format(filename)

    image = models.FileField(max_length=250, upload_to=get_picture_url, verbose_name='Изображение')
    
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


class ExternalLink(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    url = models.URLField(max_length=250, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Внешняя ссылка'
        verbose_name_plural = 'Внешние ссылки'

    def __str__(self):
        return self.title


class MailToString(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Кому отправлять письмо'
        verbose_name_plural = 'Кому отправлять письмо'

    def __str__(self):
        return self.email


class MailFromString(models.Model):
    use_tls = models.BooleanField(verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)')
    use_ssl = models.BooleanField(verbose_name='EMAIL_USE_SSL(yandex.ru)')
    port = models.PositiveIntegerField(verbose_name='EMAIL_PORT')
    host = models.CharField(max_length=250, verbose_name='EMAIL_HOST')
    host_user = models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER')
    host_password = models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD')

    class Meta:
        verbose_name = 'Откуда отправлять письмо'
        verbose_name_plural = 'Откуда отправлять письмо'

    def __str__(self):
        return self.host_user