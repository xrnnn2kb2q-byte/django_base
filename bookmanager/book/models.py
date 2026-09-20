from django.db import models

# Create your models here.

'''
    1.模型类需要继承自 models.Model
    2.系统会自动添加一个主键 id
    3.字段
        字段名 = model.类型(选项)
        
        字段名其实就是数据表的字段名
        字段名不要使用python、mysql等关键字
        
        char(M)
        varchar(M)
        M就是选项
'''
class Book(models.Model):
    # id
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键的表：人物属于哪本书
    book = models.ForeignKey(Book, on_delete=models.CASCADE)