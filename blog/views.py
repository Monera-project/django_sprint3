from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, Category


def get_filtered_posts():
    """Возвращает отфильтрованные посты для отображения на сайте."""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related('author', 'location', 'category')


def index(request):
    post_list = get_filtered_posts()[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('author', 'location', 'category')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
