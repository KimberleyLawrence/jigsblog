from django.shortcuts import render as _render
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

#
from django.core import serializers


@login_required
def render(request, template, render_keys):
    try:
        render_keys['debug_posts'] = Post.objects.filter(user=request.user)
    except Exception:
        pass
    return _render(request, template, render_keys)

# Create your views here.

#_____________index________________
@login_required
def index(request):
    posts = Post.objects.all().order_by('-postdate')

    return render(request,'index.html',{
        'posts': posts,

    })


#_____________post_new________________
@login_required
def post_new(request, post_id=None):
    print "post_new", post_id
    form = PostForm({'user':request.user})
    post = None

    try:
        post = Post.objects.get(id=post_id)
    except Exception:
        pass

    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            messages.success(request, 'Your post was successful, thank you!')
            return HttpResponseRedirect(reverse('index') + "#{0.id}-{0.title}".format(post))
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'post.html',
        {
            'form': form,
            'post_id': post_id,
            'post': post,
            'edit_or_create_post': True,
        }
    )

#__________api view - post_get __________________
@login_required
def post_get(request, post_offset=0, number_of_posts=5):
    # Query the posts
    start = int(post_offset)
    end = start + int(number_of_posts)
    all_posts = Post.objects.all().order_by('-postdate')[start:end]

    # Turn into into JSON for jQuery
    # data = serializers.serialize("json", [p.__dict__ for p in posts])
    import json
    posts = [p.json() for p in all_posts]
    data = {
        'post_offset': post_offset,
        'number_of_posts': number_of_posts,
        'start': start,
        'end': end,
        'posts': posts
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


#_____________post_new________________
@login_required
def post_manage(request):
    """ List all my posts for me to view and edit..."""
    posts = Post.objects.filter(user=request.user)
    return render(request,'post_manage.html',{
        'posts': posts,
    })


#___________post_delete___________
@login_required
def post_delete(request, post_id=None):
    print "post_delete", post_id


    try:
        post = Post.objects.filter(id=post_id).filter(user=request.user)
    except Exception:
        pass


    post.delete()
    messages.success(request, 'Your post was successfully deleted')
    return HttpResponseRedirect(reverse('post_manage'))
