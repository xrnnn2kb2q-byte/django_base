from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.

def index(request):

    # 在这里实现 增删改查
    books = BookInfo.objects.all()
    print(books)

    return HttpResponse("index")

#######################增加数据#######################

from book.models import BookInfo

# 方式1
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 必须要调用 对象的save方法才能将数据保存到数据库中
book.save()

# 方式2
# objects -- 相当于一个代理 实现增删改查
#
BookInfo.objects.create(
    name = '测试开发',
    pub_date='2000-1-1',
    readcount=100
)

#######################修改数据#######################

# 方式1
# select * from bookinfo where id=6
book = BookInfo.objects.get(id=6)

book.name = '运维开发入门'

# 想要保存数据 需要调用 对象的save方法
book.save()

# 方式2
# filter 过滤
BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=666)

# 错误的
# BookInfo.objects.get(id=5).update(name='5555',commentcount=999)

#######################删除数据#######################

# 方式1

book = BookInfo.objects.get(id=6)

# 删除分2种，物理删除（这条记录的数据删除） 和 逻辑删除 （修改标记位 例如 is_delete=False）

book.delete()

# 方式2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()

#######################查询数据#######################

# get查询单一结果，如果不存在会抛出模型类，DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果
books = BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

#######################过滤查询#######################
# 实现SQL中的where功能，包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果 n = 0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果 n = 0,1,2,...
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)           # 简写形式
book = BookInfo.objects.get(id__exact=1)    # 完整形式 (id_exact=1)
book = BookInfo.objects.get(pk=1)           # pk primary key 主键

BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

# 查询书名中包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大于3的图书
# 大于 gt         great 大
# 大于等于 gte     e  equal
# 小于 lt
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-01-01')