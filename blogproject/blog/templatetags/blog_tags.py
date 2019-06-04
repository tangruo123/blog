from ..models import Article, Category, Slideshow, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()


# 轮播图
@register.simple_tag
def get_slide():
    return Slideshow.objects.all()


# 最新文章
@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


# 文章归档
@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


# 文章分类
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)


# 标签云
@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)


# 阅读量最多的文章
@register.simple_tag
def get_max_articles(num=5):
    return Article.objects.all().order_by('-views')[:num]


# 分类文章列表
@register.simple_tag
def get_categorie_list():
    article_categorie_list = {}
    for category in Category.objects.all():
        article_categorie_list[category] = []
        for article in Article.objects.filter(category=category).order_by('-created_time')[:3]:
            article_categorie_list[category].append(article)
    return article_categorie_list

