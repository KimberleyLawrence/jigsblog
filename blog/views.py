from django.shortcuts import render as _render
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def render(request, template, render_keys):
    render_keys['debug_posts'] = Post.objects.all()
    return _render(request, template, render_keys)

# Create your views here.
#@login_required
#_____________index________________
def index(request):
    posts = Post.objects.all()

    return render(request,'index.html',{
        'posts': posts,

    })

#@login_required
def post_new(request, post_id=None):
    print "post_new", post_id
    form = PostForm()
    post = None

    try:
        post = Post.objects.get(id=post_id)
    except Exception:
        pass

    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            print form.save()
            messages.success(request, 'Your post was successful, thank you!')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'post.html',
        {
            'form': form,
            'post_id': post_id,
            'post': post,
        }
    )
