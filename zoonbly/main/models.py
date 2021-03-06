from itertools import product
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) #상품명
    writer = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    marcket = models.CharField(max_length=200) # 마켓명
    pub_date = models.DateTimeField(auto_now=True) # 등록날짜
    price = models.PositiveIntegerField() # 가격
    category = models.CharField(max_length=50)
    description = models.TextField() #설명
    image = models.ImageField(upload_to = "product/image", blank=True, null=True) # 상품 이미지
    detailImage = models.ImageField(upload_to = "product/detailimage", blank=True, null=True) # 상품 상세 이미지

    def summary(self):
        return self.description[:20]

    def title(self):
        return self.name[:7]

class Options(models.Model):
    color = models.CharField(max_length=50) # 색상
    size = models.CharField(max_length=50) # 사이즈
    stock = models.PositiveIntegerField() # 수량
    price = price = models.PositiveIntegerField() # 가격
    writer = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    added = models.DateTimeField() # 작성날짜
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options') # 해당상품


class Question(models.Model):
    content = models.TextField() # 질문 내용
    writer = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    created = models.DateTimeField() # 작성시간
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions') # 해당 상품

class Answer(models.Model):
    content = models.TextField() # 답변 내용
    writer = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    created = models.DateTimeField() # 작성시간
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers') # 해당 질문
