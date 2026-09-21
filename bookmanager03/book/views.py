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

######################cookie和session############################

"""
    第一次请求，携带 查询字符串
    http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
    服务器接收到请求之后，获取username，服务器设置cookie信息，cookie信息包括username
    浏览器接收到服务器的响应之后，应该把cookie保存起来
    
    第二次及其之后的请求，我们访问http://127.0.0.1:8000/ 都会携带cookie信息，服务器就可以读取cookie信息，来判断用户身份
"""

def set_cookie(request):
    # 1. 获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2. 服务器设置cookie信息
    # 通过响应对象.set_cookie方法
    response = HttpResponse("set_cookie")
    # key, value=''
    # max_age 是一个秒数 从响应开始 计数的一个秒数
    response.set_cookie('name',username,max_age=60*60)
    response.set_cookie('pwd',password)

    return response

def get_cookie(request):
    # 获取cookie
    print(request.COOKIES)
    name = request.COOKIES.get('name')
    return HttpResponse(name)

################################################################

# session 是保存在服务器端  -- 数据相对安全
# session 需要依赖于 cookie

"""
    第一次请求 http://127.0.0.1:8000/set_session/?username=itheima   我们在服务器端设置session信息
    服务器同时会生成一个sessionid的cookie信息
    浏览器接收到这个信息之后，会把cookie数据保存起来
    
    第二次及其之后的请求 都会携带这个sessionid 服务器会验证这个sessionid 验证没有问题会读取相关数据，实现业务逻辑
"""

def set_session(request):

    # 1. 模拟 获取用户信息
    username = request.GET.get('username')
    user_id = 1

    # 2. 设置session信息
    # 假如 我们通过模型查询 查询到了用户信息
    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session里的数据，但是key有保留
    # request.session.clear()
    # # flush 是删除所有的数据，包括key
    # request.session.flush()

    request.session.set_expiry(3600)

    return HttpResponse("set_session")

def get_session(request):

    user_id = request.session.get('user_id')
    username = request.session.get('username')
    content = "{},{}".format(user_id, username)

    return HttpResponse(content)

