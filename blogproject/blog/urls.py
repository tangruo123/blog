from django.urls import path
from django.conf.urls import url
from . import views

# 在使用反向路由时会用到
app_name = 'blog'
urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^index/$', views.index, name='index'),
    # 文章详情
    # url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    # 文章归档
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # 文章分类
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # 标签云
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # 关于
    url(r'^about/$', views.about, name='about'),
    # 注册
    url(r'^register/$', views.user_register, name='register'),
    # 登录
    url(r'^login/$', views.user_login, name='login'),
    # 注销
    url(r'^logout/$', views.user_logout, name='logout'),
    # 评论
    url(r'^comment/article/(?P<post_pk>[0-9]+)/$', views.article_comment, name='article_comment'),
]