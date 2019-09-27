from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
def index(request):
    return HttpResponse("hello,welcome 天伦网络有限公司")
def register(request):
    return HttpResponse("register")
def company(request):
    """模拟使用的伪数据"""
    data = [
        {
            "date": '2016-05-02',
            "name": '高文',
            "address": '上海市浦东新区中科路2635弄'
        },
        {
            "date": '2016-05-02',
            "name": '高文1',
            "address": '上海市浦东新区中科路2636弄'
        },
        {
            "date": '2016-05-02',
            "name": '高文2',
            "address": '上海市浦东新区中科路2637弄'
        },
        {
            "date": '2016-05-02',
            "name": '高文3',
            "address": '上海市浦东新区中科路2638弄'
        }
    ]
    return JsonResponse({'code': 0, 'message': data})
# Create your views here.
