from django.contrib import admin
from .models import Category, Tag, Article, Slideshow, User, Comment
from django.contrib.auth.admin import UserAdmin


# 装饰器代替admin.site.register(Article, ArticleAdmin)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段顺序
    list_display = ['pk', 'title', 'created_time', 'modified_time', 'category']
    # 过滤字段
    list_filter = ['created_time']
    # 搜索字段
    search_fields = ['body', 'title', 'excerpt']
    # 分页,每5条为一页
    # list_per_page = 5

    # 添加、修改页属性
    # 字段排序顺序
    # fields = ['title', 'created_time', 'modified_time', 'category']
    # 给属性分组，不能和fields同时使用
    '''
    fieldsets = [
        ("content", {"fields": ['title', 'body']}),
        ("info", {"fields": ['created_time']}),
    ]
    '''
    # 自定义方法，list_display = [content]
    '''
    def content(self):
        return self.title
    '''
    # 设置页面列的名称
    # content.short_description = '标题'


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Slideshow)
admin.site.register(Comment)

admin.site.register(User, UserAdmin)