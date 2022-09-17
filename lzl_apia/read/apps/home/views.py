from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView,DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from home.filter import BookFilterSet, ZJFileter, BookSearchFileter
from read.utils.response import APIResponse
from home.page import MyPageNumberPagination,ZhangjiePageNumber,CommentPage
from home import serializer
from home import models


# Create your views here.
# 获取所有书籍、书籍详情
class BookListView(ViewSetMixin, ListAPIView, RetrieveAPIView):

    queryset = models.Book.objects.all()
    serializer_class = serializer.SerializerBooks

    filter_backends = [DjangoFilterBackend, ZJFileter, OrderingFilter]
    # 过滤
    filter_fields = ['tag', 'gender_type' ]
    # 过滤类
    filter_class = BookFilterSet
    # 排序
    ordering_fields = ['click_num', 'zhangjie', 'create_time','comment_num']

    # 分页
    pagination_class = MyPageNumberPagination


# 搜索功能!
class BookSearchView(ViewSetMixin, ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.SerializerBooks

    filter_backends = [BookSearchFileter]

    # 分页
    pagination_class = MyPageNumberPagination


# 获取频道接口
class GenderView(ViewSetMixin, ListAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializer.SerializerGender


# 获取分类
class TagView(ViewSetMixin, ListAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializer.SerializerTag


from rest_framework.filters import SearchFilter

# 评论功能
class Comment(ViewSetMixin, ListAPIView,CreateAPIView):

    queryset = models.Comment.objects.all().order_by('-create_time')
    serializer_class = serializer.SerializerComment

    from .filter import Commentfilter

    filter_backends = [DjangoFilterBackend, Commentfilter]

    filter_fields = ['user', 'book']

    pagination_class = CommentPage


from django.core.cache import cache
class BannerView(ViewSetMixin,ListAPIView):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.SerializerBanner

    def list(self, request, *args, **kwargs):
        if cache.get('banner_list'):
            print('缓存')
            return APIResponse(data=cache.get('banner_list'))

        response = super().list(request, *args, **kwargs)
        cache.set('banner_list',response.data)
        print('数据库')
        return APIResponse(data=response.data)

# 获取小说内容接口
class ZJDetail(ViewSetMixin, ListAPIView):

    queryset = models.BookZhangjie.objects.all()
    serializer_class = serializer.SerializerDetail

    filter_backends = [DjangoFilterBackend]

    filter_fields = ['book',]

    # pagination_class = MyPageNumberPagination

###########################
# 这次是真的获取小说内容的接口 #
###########################
class ZhangjieDetailView(ViewSetMixin,RetrieveAPIView):

    queryset = models.ZhangjieDetail.objects.all()
    serializer_class = serializer.ZhangjieDetailSerializer
    from .filter import CommentNameFileter
    filter_backends = [CommentNameFileter]


###########################
# 搭配小说使用的序列化        #
###########################
class zhangjiePage(ViewSetMixin,ListAPIView):

    queryset = models.BookZhangjie.objects.all()
    serializer_class = serializer.SerializerDetail

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['book', 'detail' ]
    from .page import zhangjieneirong
    pagination_class = zhangjieneirong


# 书架的接口
class Shujiaview(ViewSetMixin,ListAPIView,CreateAPIView,DestroyAPIView):

    queryset = models.ShuJia.objects.all ()

    serializer_class = serializer.ShujiaSerializer

    filter_backends = [DjangoFilterBackend,]

    filter_fields = ['user']

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)
        # print('我走到这里')
        return APIResponse()
