from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('allbook', views.BookListView, 'allbook')
router.register('searchbook', views.BookSearchView, 'searchbook')
router.register('gender', views.GenderView, 'gender')
router.register('tag', views.TagView, 'tag')
router.register('zjdetail', views.ZJDetail, 'zjdetail')
router.register('comment', views.Comment, 'comment')
router.register('banner', views.BannerView, 'banner')
router.register('zhangjiedeaile', views.ZhangjieDetailView, 'zhangjiedeaile')
router.register('shujia', views.Shujiaview, 'shujia')
router.register('zhangjiepage', views.zhangjiePage, 'zhangjiepage')

urlpatterns = [
    path('', include(router.urls), )
]
