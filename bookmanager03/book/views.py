from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.

def create_book(request):

    book = BookInfo.objects.create(
        name = 'abc',
        pub_date = '2000-1-1',
        readcount = 10
    )

    return HttpResponse("create")

def shop(request,city_id, shop_id):

    query_params = request.GET
    print(query_params)
    # < QueryDict: {} >
    # QueryDict 具有字典的特性
    return HttpResponse("shop")

#########################
'''
    查询字符串
    http://ip:port/path/path/?key=value&key1=value1
    
    url 以 ？为分割 分为两部分
    ？前边为 请求路径
    ？后变为 查询字符串  查询字符串 类似于字典 key=value 多个数据用&连接
    
    
'''

def register(request):
    data = request.POST
    print(data)
    return HttpResponse("register")

def json(request):
    # request.POST json数据不能通过request.POST获取数据
    body = request.body
    print(body.decode())

    # JSON形式的字符串 可以转换为 python的字典
    import json
    body_dict = json.loads(body.decode())
    print(body_dict)

    return HttpResponse('json')
