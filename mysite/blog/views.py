from django.shortcuts import render, get_object_or_404

from .models import BlogArticles
# 基于函数的视图，这个函数叫视图函数
# 函数的参数是request，这个参数负责响应所接受到的请求且不能缺少
# 并总位于第一的位置，还可以根据需要在后面增加别的参数。
def blog_title(request):
    # 得到所有的BlogArticles对象实例。
	blogs = BlogArticles.objects.all()
    # 将数据渲染到指定模板上。
    # 第1个参数必须是request
    # 然后是模板位置和所传达的数据。
    # 数据是用字典形式传达给模板的。
	return render(request, "blog/titles.html", {"blogs":blogs})

# 多了一个参数，该参数用于传递文章的id
def blog_article(request, article_id):
	#rticle = BlogArticles.objects.get(id=article_id)
    # 简化对请求网页不存在时的异常处理。
	article = get_object_or_404(BlogArticles, id=article_id)
	pub = article.publish
	return render(request, "blog/content.html", {"article":article, "publish":pub })
