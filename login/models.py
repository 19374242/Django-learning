from django.db import models

# Create your models here.
# 这里写数据库封装类

from django.db import models


class User(models.Model):
    # 别忘了主键，必须要写
    name = models.CharField(max_length=100, blank=True, null=False, primary_key=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
