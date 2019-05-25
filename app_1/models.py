from django.db import models


# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=8)
    password=models.CharField(max_length=8)
    '''
    用户表
    '''

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'


class Blogs(models.Model):
    '''
    博客表
    '''
    blog_title = models.CharField(verbose_name='博客标题', max_length=100)
    blog_matter = models.TextField(verbose_name='博客正文')
    blog_type_id = models.ForeignKey('Blogs_type', on_delete=models.CASCADE, verbose_name='博客类别')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户名')
    write_time = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = '博客表'
        verbose_name_plural = '博客表'


class Blogs_type(models.Model):
    '''
    博客类别表
    '''
    b_type = models.CharField(verbose_name='博客类别', max_length=30)

    def __str__(self):
        return self.b_type

    class Meta:
        verbose_name = '博客类别表'
        verbose_name_plural = '博客类别表'