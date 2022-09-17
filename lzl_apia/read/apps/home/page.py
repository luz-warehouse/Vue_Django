
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):

    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 50
    
class ZhangjiePageNumber(PageNumberPagination):

    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1

# 评论分页
class CommentPage(PageNumberPagination):

    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 20


# 搭配小说使用的章节分页

class zhangjieneirong(PageNumberPagination):

    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1