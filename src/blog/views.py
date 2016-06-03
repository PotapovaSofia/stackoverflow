from django.views.generic.detail import DetailView
from blog.models import Blog
from django.views.generic.list import ListView
from django.db.models import Count


class BlogView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

class BlogList(ListView):
    template_name = "blog/blog_list.html"
    model = Blog

    def get_queryset(self):
        blogSet = Blog.objects.all()

        blogSet = blogSet.annotate(events_count=Count('event__id'))
        return blogSet[:10]