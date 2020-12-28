from .models import BLOG, COMMENT


def global_context(request):
    latest_post = BLOG.objects.filter(published=True).order_by('-date')[0:2]

    return {
        'latest_post': latest_post,
    }

