from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    # 이미지 url 을 저장
    image = models.URLField()
    # 장바구니
    # related_name : 역참조 시 사용할 이름
    # null값 허용 : blank = True
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cart", blank=True
    )
