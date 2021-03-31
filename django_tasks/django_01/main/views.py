from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from main.models import Post
from main.forms import PostForm


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About Company"})


def posts(request):
    _posts = Post.objects.all()
    return render(request, "main/posts.html", {'title': "Posts", "posts": _posts})


def post_create(request):
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = "Cannot save the post"
    else:
        form = PostForm()
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, "main/post_create.html", context=context)


def api_posts(request):
    _posts = Post.objects.all()
    response_data = [dict(title=post.title, description=post.description, content=post.content) for post in _posts]
    return JsonResponse(response_data, safe=False)
