from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
	title = models.CharField(max_length=300)
    # 通过author规定了博客文章和用户之间的关系——一个用户对于多篇文章，
    # ForeignKey()就反映了这种“一对多”关系。类User就是BlogArticle的对应对象，
    # related_name='blog_posts'的作用是允许通过反向查询到BlogArticles
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)

    # 通过ordering = ("-publish",)，规定了BlogArticles实例对象的显示顺序，即按照publish
    # 字段值倒序显示。
	class Meta:
		ordering = ("-publish",)

	def __str__(self):
		return self.title