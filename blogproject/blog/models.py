from django.db import models
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser


# 用户
class User(AbstractUser):
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


# 文章分类
class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    日期时间类型 DateTimeField、整数类型 IntegerField
    """
    name = models.CharField(max_length=100, verbose_name='文章分类名')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='文章标签名')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=70, verbose_name='文章标题')
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(verbose_name='文章内容')
    img = models.ImageField(upload_to="static/blog/img/%Y/%m/%d", verbose_name='文章缩略图')
    # 文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(verbose_name='文章创建时间')
    modified_time = models.DateTimeField(verbose_name='文章最后修改时间')
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='文章摘要')
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # models.ForeignKey() 需要指定on_delete=models.CASCADE，不然会报错
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类名')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签名')
    views = models.PositiveIntegerField(default=0, verbose_name='文章阅读量')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='作者')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    # 增加阅读量
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 自动填写摘要
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Article, self).save(*args, **kwargs)


# 轮播图
class Slideshow(models.Model):
    # 标题
    title = models.CharField(max_length=70, verbose_name='轮播图标题')
    # 图片
    img = models.ImageField(upload_to="static/blog/img/%Y/%m/%d", verbose_name='轮播图')
    # 图片指向的文章
    article = models.OneToOneField(Article, on_delete=models.CASCADE, default='', verbose_name='指向的文章')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.article.id})

    def __str__(self):
        return self.title


# 评论
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='用户名')
    email = models.EmailField(max_length=255, verbose_name='用户邮箱')
    text = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, verbose_name='评论文章')
    # pid = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]


# 留言
'''
class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='用户名')
    email = models.EmailField(max_length=255, verbose_name='用户邮箱')
    text = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    pid = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='父级留言')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]
'''



