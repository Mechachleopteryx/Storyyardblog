from django.shortcuts import render, get_object_or_404, redirect
from .models import BLOG, COMMENT
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from contacts.models import Contact


def home(request):
    blogs = BLOG.objects.filter(published=True).order_by('-date')[0:2]
    allblogs = BLOG.objects.all()

    search_result = search_filter(request)

    context = {
        'blogs': blogs,
        'allblogs': allblogs,
        'search_result': search_result
    }
    if search_result:
        return render(request, 'search_result.html', context)
    return render(request, 'index.html', context)


def blog(request):
    blogs = BLOG.objects.all()
    latests = BLOG.objects.filter(published=True).order_by('-date')[0:5]

    search_result = search_filter(request)

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
        'latests': latests,
        'page_object': page_object,
        'search_result': search_result,
    }
    if search_result:
        return render(request, 'search_result.html', context)
    return render(request, 'blog.html', context)


def detail(request, pk):
    blogs = BLOG.objects.get(id=pk)
    latests = BLOG.objects.filter(published=True).order_by('-date')[0:5]

    search_result = search_filter(request)

    comments = COMMENT.objects.filter(post=blogs).order_by('-created')
    comment_number = comments.count()

    if request.method == 'POST':
        author = request.POST.get('authorname', False)
        email = request.POST.get('author_email', False)
        text = request.POST.get('comment', False)
        comment_form = COMMENT(post=blogs, author=author,
                               email=email, text=text, approved=True)

        # Checkking if comment already exits
        if not comments.filter(author=author, post=blogs, email=email, text=text).exists():
            comment_form.save()

    context = {
        "blogs": blogs,
        'latests': latests,
        'comments': comments,
        'comment_number': comment_number,
        'search_result': search_result
    }
    if search_result:
        return render(request, 'search_result.html', context)
    return render(request, 'post.html', context)


def search_filter(request):
    result = ''
    if request.method == 'POST':
        quary = request.POST.get('searchfield', False)
        result = BLOG.objects.all().filter(title__contains=quary)
        print('Qaury is', quary)
        print('Result is', result)
        return result


def search_results(request):
    allblogs = BLOG.objects.all()
    context = {
        'allblogs': allblogs
    }
    return render(request, 'search_result.html', context)


def contact(request):

    contacts = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['user_email']
        subject = request.POST['subj']
        message = request.POST['msg']

        new_contact = Contact(name=name, email=email,
                              subject=subject, message=message)

        if not contacts.filter(name=name, email=email,
                               subject=subject, message=message).exists():
            new_contact.save()

    return render(request, 'contact.html', context=None)
