from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, name='title')
    mail = models.EmailField(null=False, blank=False, name='mail', default='ali@mail.com')
    description = models.CharField(max_length=3000, null=True, blank=True, name='description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        verbose_name = 'Книги'
        verbose_name_plural = 'книга'
