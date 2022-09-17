from django_filters.filterset import FilterSet
from django_filters import filters
from . import models
from django.db.models import Q

from rest_framework.filters import BaseFilterBackend
class ZJFileter(BaseFilterBackend):
    # 章节过滤
    def filter_queryset(self, request, queryset, view):
        zhangjie = request.query_params.get('zhangjie')

        if zhangjie:

            if int(zhangjie) < 500:
                queryset = queryset.filter(zhangjie__lt = 500)
                return queryset
            elif int(zhangjie) >500 and int(zhangjie) < 1000:
                queryset = queryset.filter(zhangjie__gt=500,zhangjie__lt = 1000)
                return queryset
            else:
                queryset = queryset.filter(zhangjie__gt=1000)
                return queryset
        return queryset


class BookFilterSet(FilterSet):
    # 实现了区间过滤
    min_zj = filters.NumberFilter(field_name='zhangjie', lookup_expr='gte')

    max_zj = filters.NumberFilter(field_name='zhangjie', lookup_expr='lte')

    class Meta:
        model = models.Book
        fields = ['tag','gender_type','max_zj','min_zj']


# class ZhangjieDetailViewFilterSet(BaseFilterBackend):
#
#     def filter_queryset(self, request, queryset, view):
#
#         book = request.query_params.get('book')
#
#         queryset_list = []
#         # print(queryset[1].__dict__)
#         all = models.Book.objects.filter(pk=book).first().bookzhangjie.all()
#         print(queryset)
#         for obj in all:
#
#             didi = models.BookZhangjie.objects.filter(pk=obj.detail.id).first()
#             print(didi)
#             # dic = {
#             #     'id':obj.detail.id,
#             #     'content':obj.detail.content
#             # }
#             queryset_list.append(didi)
#             # print(dic)
#         # print(queryset)
#         return queryset_list


# 全文搜索
class BookSearchFileter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name')

        if name:
            queryset = queryset.filter(Q(name__contains=name)|Q(author__name__contains=name)|Q(tag__name__contains=name))
        return queryset


class Commentfilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        username = request.query_params.get('username')



        if username:
            queryset_list = []

            for obj in queryset:

                if obj.user.username == username:
                    queryset_list.append(obj)

            return queryset_list

        return queryset



# 再次测试
from rest_framework.filters import BaseFilterBackend
class CommentNameFileter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        # print(request.get('book'))
        # print(request.query_params.get('book'))
        # print(request.query_params.get('book'))
        book_id = request.query_params.get('book')

        # print(queryset[0].bookzhangjie.book.id)

        res = queryset.filter(bookzhangjie__book__id=book_id)

        return res