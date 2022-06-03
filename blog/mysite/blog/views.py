from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_list')

class PostDetailView(generic.DetailView):
    model = Post
    
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_detail')
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')