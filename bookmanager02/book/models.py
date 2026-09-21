from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

"""
    1.模型类 需要继承自 models.Model
    2.定义属性
        属性名 = models.类型(选项)
        
        2.1 属性名 对应 就是字段名
            不要使用python，MySQL关键字
            不要使用连续的下划线(__)
        2.2 类型 MySQL的类型
        2.3 选项  是否有默认值，是否唯一，是否为null
            CharField必须设置 max_length
            verbose_name 主要是 admin 站点使用
    3.改变表的名称
        默认表的名称是：    子应用名_类名 都是小写
        修改表的名字
        
create table 'qq_user'(
    id int,
    name varchar(10) not null default '',
    
)
"""

class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = IntegerField(default=0)
    commentcount = IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    # 一对多的关系模型中
    # 系统会为我们自动添加一个 关联模型类名小写_set
    # peopleinfo_set = [PeopleInfo, PeopleInfo, ...]

    class Meta:
        db_table = 'bookinfo' # 修改表的名字
        verbose_name = '书籍管理' # admin站点使用的（了解）

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )

    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加    id

    # 外键的级联操作
    # 主表 和 从表
    # 1 对 多
    # 书籍 对 人物

    # 主表的一条数据 如果删除了
    # 从表有关联的数据 关联的数据怎么办呢？
    # SET NULL
    # 抛出异常，不让删除
    # 级联删除

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name