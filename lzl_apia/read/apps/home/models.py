from django.db import models
# from user.models import  User
# Create your models here.

# 等级经验对照表
class Level_ex(models.Model):

    level = models.IntegerField('等级',unique=True)

    ex = models.IntegerField('经验')

    class Meta:

        db_table = 'level'  # 表名
        verbose_name = '经验对照表'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name

# 设置经验奖励
class Ex_detail(models.Model):

    sign_in = models.IntegerField('签到经验',default=10)

    down_load = models.IntegerField('下载经验',default=10)

    up_load = models.IntegerField('上传经验',default=100)

    class Meta:

        db_table = 'level_detail'  # 表名
        verbose_name = '经验详情表'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name


# 男频女频表
class Gender(models.Model):

    choose = [
        (1,'男频'),
        (2,'女频'),
    ]

    gender = models.IntegerField('男女频道分类',choices=choose,default=1)

    def gender_name(self):

        return self.get_gender_display()

# 分类表
class Tag(models.Model):

    name = models.CharField('分类名字',max_length=32)

    # is_free = models.BooleanField('是否免费',default=1)

    class Meta:

        db_table = 'tag'  # 表名
        verbose_name = '分类'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name


# 作者表
class Author(models.Model):

    name = models.CharField('作者名字',max_length=32)
    author_img = models.ImageField(upload_to='author', default='author/man.png')


# 书
class Book(models.Model):

    book_img = models.ImageField(upload_to='book', default='book/man.png')

    name = models.CharField('书名',max_length=32)
    desc = models.CharField('简介',max_length=255)
    click_num = models.IntegerField('点击数',default=0)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    # # 章节数
    zhangjie = models.IntegerField('书的章节数',null=True)
    # 书籍和分类一对多
    tag = models.ForeignKey(verbose_name='书籍和分类一对多',to='Tag',on_delete=models.CASCADE,db_constraint=False,related_name='book')
    # 书籍和作者一对多
    author = models.ForeignKey(verbose_name='书籍和作者一对多',to='Author',on_delete=models.CASCADE,db_constraint=False,related_name='book')
    # 书籍和频道一对多
    gender_type = models.ForeignKey(to='Gender',on_delete=models.CASCADE,db_constraint=False,related_name='book')
    # 评论数
    comment_num = models.IntegerField('评论数',default=0)

    class Meta:

        db_table = 'book'  # 表名
        verbose_name = '书名'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.name

    @property
    def bookzj(self):
        book_list = []
        for zj in self.bookzhangjie.all():
            # print(zj)
            book_list.append({'id':zj.id,'name':zj.name})
        return book_list

    @property
    def same_type(self):
        # print('这是打印')
        import json
        book_list_obj = self.tag.book.all()

        book_list = []

        for book_obj in book_list_obj:

            if len(book_list)>=3:

                return json.dumps(book_list)

            dic = {
                'id':book_obj.id,
                'img':str(book_obj.book_img),
                'desc':book_obj.desc,
                'name':book_obj.name
            }

            book_list.append(dic)

        return json.dumps(book_list)


# 书的章节
class BookZhangjie(models.Model):

    name = models.CharField('章节名字',max_length=32)
    book = models.ForeignKey(to='Book',on_delete=models.CASCADE,db_constraint=False,related_name='bookzhangjie')
    detail = models.OneToOneField(to='ZhangjieDetail',on_delete=models.CASCADE,db_constraint=False,related_name='bookzhangjie')

    class Meta:

        db_table = 'BookZhangjie'  # 表名
        verbose_name = '章节表'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def ZJ_id(self):

        # print(self.detail.content)

        return self.detail.id

    def num(self):
        print(self.book.bookzhangjie.count())

        return self.book.bookzhangjie.count()


# 章节内容表
class ZhangjieDetail(models.Model):



    content = models.TextField('内容')

    class Meta:
        db_table = 'ZhangjieDetail'  # 表名
        verbose_name = '章节内容'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name

    @property
    def zj_name(self):

        return self.bookzhangjie.name

    @property
    def zj_book(self):
        print(self.bookzhangjie.book.id)

        return self.bookzhangjie.book.id

import datetime
# 评论表
class Comment(models.Model):

    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
        verbose_name='评论和书一对多',
        db_constraint=False,
        related_name='comment',
    )

    user = models.ForeignKey(to='user.User',on_delete=models.CASCADE,verbose_name='用户和评论一对多',db_constraint=False,related_name='comment')

    create_time = models.DateTimeField('评论时间',auto_now_add=True)

    parent = models.ForeignKey(to='self',null=True,blank=True,on_delete=models.CASCADE)

    com_num = models.IntegerField('第几次评论,用来做子评论的多人评论',default=0)

    context = models.CharField(max_length=32,verbose_name='评论内容')

    def parent_user(self):

        if self.parent:
            # print(self.parent)
            # print(self.parent.user.username,self.parent.user.nickname)
            return self.user.nickname
        else:
            return
    # import json
    # 同类型
    def same_type(self):
        import json
        book_list_obj = self.book.tag.book.all()

        book_list = []

        for book_obj in book_list_obj:

            if len(book_list)>=3:

                return json.dumps(book_list)

            dic = {
                'id':book_obj.id,
                'img':str(book_obj.book_img),
                'desc':book_obj.desc,
                'name':book_obj.name
            }

            book_list.append(dic)

        return json.dumps(book_list)

    # 书名字
    def bookname(self):

        return self.book.name

    # 用户名
    def username(self):

        return self.user.username
    # 昵称
    def nickname(self):

        return self.user.nickname
    # 用户头像
    def user_img(self):

        return self.user.icon

    class Meta:
        db_table = 'Comment'  # 表名
        verbose_name_plural = '评论内容'

# 轮播图数据
class Banner(models.Model):
    '''轮播图'''
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否上架')
    orders = models.IntegerField(verbose_name='优先级')
    title = models.CharField(max_length=16, unique=True, verbose_name='名称')
    image = models.ImageField(upload_to='banner', verbose_name='图片', help_text='必须传入指定规格大小3840*800')
    link = models.CharField(max_length=64, verbose_name='跳转连接')
    info = models.TextField(verbose_name='详情')

    class Meta:
        db_table = 'banner'  # 表名
        verbose_name_plural = '轮播图'


# 书架
class ShuJia(models.Model):

    user = models.ForeignKey(to='user.User',on_delete=models.CASCADE,verbose_name='用户和书架一对多',db_constraint=False,related_name='shujia')

    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
        verbose_name='评论和书一对多',
        db_constraint=False,
        related_name='shujia',
    )
    @property
    def bookname(self):

        return self.book.name
