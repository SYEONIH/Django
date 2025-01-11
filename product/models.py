from django.db import models

# 모델 정의
class MainContent(models.Model):
 title = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateTimeField('date published')
