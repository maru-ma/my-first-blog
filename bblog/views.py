from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    # Ordenamos los posts por fecha de publicacion
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    # 'render' : reproduce, construye el template.
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # Si queremos publicaar un nuevo post
    if request.method == "POST":
        form = PostForm(request.POST)
        # Verificamos si el form es valido
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    # Obtenemos el post que queremos editar
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # Pasamos post como instancia
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # Abrimos este post como instancia cuando queremos editarlo
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
