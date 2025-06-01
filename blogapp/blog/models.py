from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Taslak'),
        ('published', 'Yayınlandı'),
    )

    title = models.CharField(max_length=200, verbose_name="Başlık")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Yazar")
    content = models.TextField(verbose_name="İçerik")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Durum")

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name="Kullanıcı Adı")
    password = models.CharField(max_length=128, verbose_name="Şifre")
    email = models.EmailField(unique=True, verbose_name="E-posta")
    first_name = models.CharField(max_length=30, verbose_name="Ad")
    last_name = models.CharField(max_length=30, verbose_name="Soyad")
    is_staff = models.BooleanField(default=False, verbose_name="Yönetici mi?")