from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm, PostForm
from .models import Post


def home(request):
    posts = Post.objects.all().order_by("-created")
    return render(
        request,
        "index.html",
        {
            "posts":posts
        }
    )

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(
        request,
        "signup.html",
        {
            "form":form
        }
    )

@login_required  
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(
        request,
        "add.html",
        {
            "form":form
        }
    )
