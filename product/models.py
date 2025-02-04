from django.db import models
from django.contrib.auth.models import User

# 모델 정의
class Product(models.Model):
    name = models.CharField(max_length=200)  # 상품 이름
    rating = models.FloatField()  # 별점
    review_count = models.IntegerField()  # 리뷰 수
    price = models.IntegerField()  # 가격
    description = models.TextField()  # 설명
    pub_date = models.DateTimeField('date published')  # 올린 일자

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # 상품
    content = models.TextField() # 댓글 내용
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
