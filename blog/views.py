from django.shortcuts import render
from django.http import  HttpResponse
from .models import Goods
from .models import Blog

from django.views.generic import View

# def index(request):
#     return HttpResponse('hellow world')
def index(request):
    return render(request,'blog/index.html')
def author_search(request):
    author_id = request.GET.get('id')
    return HttpResponse(author_id)
def add_blog(request):
    #插入
    # # blog = Blog(name="陈豪右",title="西游记")
    # # blog.save()
    #查询
    # # blog = Blog.objects.get(pk=5)
    # # blog.__str__()
    #查询
    # blog = Blog.objects.filter(title="西游记")
    # print(blog)
    #插入数据
    # goods = Goods(removed=True)
    # goods.save()
    # goods = Goods()
    # goods.save()
    # goods = Goods(email='1491047436@qq.com')
    # goods.save()
    #exclude != fliter ==
    goods = Goods.objects.filter(removed=False).exclude(email=None)
    print(len(goods))
    return HttpResponse("add data sucess")

#首页视图
class IndexView(View):
    
