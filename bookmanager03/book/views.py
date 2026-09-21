from django.http import HttpResponse
from django.shortcuts import render, redirect
from book.models import BookInfo

# Create your views here.

def create_book(request):

    book = BookInfo.objects.create(
        name = 'abc',
        pub_date = '2000-1-1',
        readcount = 10
    )

    return HttpResponse("create")

def shop(request,city_id, mobile):

    import re
    # if not re.match('\\d{5}', shop_id):
    #     return HttpResponse('没有此商品')

    query_params = request.GET
    print(query_params)
    # < QueryDict: {} >
    # QueryDict 具有字典的特性
    return HttpResponse("shop")

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

def response(request):
    # response = HttpResponse("response",status=200)
    info = {
        'name':'itcast',
        'address':'shunyi'
    }
    girl_friends = [
        {
            'name':'rose',
            'address':'shunyi'
        },
        {
            'name':'jack',
            'address':'changping'
        }
    ]
    # data 返回的相应数据 一般是字典类型
    '''
    safe = True 是表示 我们的data 是字典数据
    JsonResponse 可以吧字典转换为json
    
    现在给了一个非字典数据，出了问题 我们自己负责
    '''
    # response = JsonResponse(data=info,safe=False)
    # return response

    import json
    data = json.dumps(girl_friends)
    response = HttpResponse(data)
    # return response

    return redirect('http://www.itcast.cn')


    # 1xx
    # 2xx
    #       200 成功
    # 3xx
    # 4xx   请求有问题
    #       404 找不到页面 路由有问题
    #       403 禁止访问 权限问题
    # 5xx
    # HTTP status code must be an integer from 100 to 599

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

    ###########请求头############
    print(request.META)

    return HttpResponse('json')

def method(request):
    print(request.method)
    return HttpResponse("method")

