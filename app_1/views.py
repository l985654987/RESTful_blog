from django.shortcuts import render
from app_1 import models
from rest_framework.views import APIView
from app_1.serializers import *
from rest_framework.response import Response
# Create your views here.

class BaseResponse(object):
    def __init__(self):
        self.code=1000
        self.msg=""
        self.data=None
    @property
    def dict(self):
        return self.__dict__

#主页
class Home(APIView):
    def get(self,request):
        blogs = models.Blogs.objects.all().order_by('-write_time')
        blogs_obj = BlogsSerializer(blogs,many=True)
        return Response(blogs_obj.data)
    def post(self,request):
        receive = request.data
        key=receive.get('key')
        blogs = models.Blogs.objects.filter(blog_title__icontains=key)
        blogs_obj = BlogsSerializer(blogs, many=True)
        return Response(blogs_obj.data)

#注册
class Reg(APIView):
    def post(self,request):
        response = BaseResponse()
        receive = request.data
        username=receive.get('username')
        password = receive.get('password')
        re_password=receive.get('re_password')
        if password==re_password:
            obj = models.User.objects.create(username=username,password=password)
            response.msg='注册成功'
            response.code = 2000
        else:
            response.msg = '注册失败'
            response.code = 2000
        return Response(response.dict)

#登录
class Login(APIView):
    def post(self,request):
        response = BaseResponse()
        receive = request.data
        username = receive.get('username')
        password = receive.get('password')
        user = models.User.objects.filter(username=username, password=password)
        if user:
            response.msg = "登陆成功"
        else:
            try:
                models.User.objects.get(username=username)
                response.msg = "密码错误!"
                response.code = 1002
            except BaseException:
                response.msg = "用户不存在!"
                response.code = 1003
        return Response(response.dict)



#我的博客
class Myblog(APIView):
    def get(self,request):
        username = '{}'.format(request.user)
        blogs = models.Blogs.objects.filter(user_id__username=username)
        blogs_obj = BlogsSerializer(blogs,many=True)
        return Response(blogs_obj.data)



class Content(APIView):
    def get(self, request,id):
        print(id,type(id))
        blog = models.Blogs.objects.filter(id=id)
        print(blog)
        blogs_obj = BlogsSerializer(blog, many=True)
        return Response(blogs_obj.data)

