from django.urls import path, register_converter
from book import views
from django.urls import converters

# 1. 定义转换器
class MobileConverter:
    # 验证数据的关键是：正则
    regex = "1[3-9]\d{9}"
    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return int(value)
    # 讲匹配的结果用于反向解析传值时使用（了解）
    def to_url(self, value):
        return str(value)

register_converter(MobileConverter, 'phone')
#2. 先注册转换器，才能在第三步中使用
# converter 转换器类
# type_name 转换器名字

urlpatterns = [
    path('create/',views.create_book),

    # <转换器名字:变量名>
    # 转换器会对变量数据进行 正则的验证
    path('<int:city_id>/<phone:mobile>',views.shop),
    path('register/',views.register),
    path('json/',views.json),
    path('method/',views.method),
    path('response/',views.response),
    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),
    path('set_session/',views.set_session),
    path('get_session/',views.get_session),
    path('login/',views.login),

    #######################类视图#########################
    path('163login/',views.LoginView.as_view()),
    path('order/',views.OrderView.as_view()),
]

'''
class IntConverter:
    regex = "[0-9]+"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
'''