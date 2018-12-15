from django.contrib import admin

from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ("title", "author", "publish")
    # 设置过了选项
    list_filter = ("publish", "author")
    # 文章的搜索功能
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    # 按日期月份筛选
    date_hierarchy = "publish"
    # 按发布日期和作者排序
    ordering = ['publish', 'author']

# 将BlogArticlesAdmin注册到admin
admin.site.register(BlogArticles, BlogArticlesAdmin)
