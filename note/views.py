from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.


def home(request):
    post_list = Post.objects.order_by('-timestamp')

    paginator = Paginator(post_list, per_page=6)
   
    page = request.GET.get('page', 1)

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context ={
        'post': post_list,
        'paginator':paginator, 
        'page_obj': post_list,
    }
    return render(request, "index.html", context)




#Read Post Fucntion
def note_read(request, slug):
    post = Post.objects.get(slug =slug)
    return render(request, "note.html", {'read': post})


def archive_post(request):
    post_list = Post.objects.order_by('-timestamp')

    return render(request, "archive.html", {'post': post_list})


#Search Fucntion
def search(request):
    query = request.GET.get('q')
    search_results = Post.objects.filter( Q(title__icontains=query) | Q(content__icontains=query) )

    return render(request, "search.html", {'results':search_results})
