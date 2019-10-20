from django.db import models
from django.urls import reverse
from uuid import uuid1
from core.models import SEO


class DocumentCategory(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_absolute_url(self):
        return reverse('document_category', args=[self.slug])

    class Meta:
        verbose_name = 'Категория документов'
        verbose_name_plural = 'Категории документов'

    def __str__(self):
        return self.title


class Document(models.Model):
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='documents')
    name = models.TextField(verbose_name='Название документа', unique=True)

    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'documents/{0}/{1}'.format(self.category.slug, filename)

    document = models.FileField(upload_to=get_document_url, max_length=500, verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name