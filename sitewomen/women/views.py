from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.services import get_menu
from women.forms import PostForm, CommentForm
from women.models import Post, Comment


class PostListView(ListView):
    queryset = Post.objects.prefetch_related('tags').filter(is_published=True)
    context_object_name = 'posts'
    template_name = 'women/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = get_menu(self.request)
        return context


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': get_menu(request)})


class PostDetailView(DetailView):
    template_name = 'women/post.html'
    model = Post

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['post_slug'])

    def get_context_data(self, *args, **kwargs):
        post = self.get_object()
        context = super().get_context_data(*args, **kwargs)
        context['menu'] = get_menu(self.request)
        context['comments'] = Comment.objects.filter(post=post, parent=None)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(CreateView):
    template_name = 'women/add_post.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        return super().form_valid(new_post)

    def get_success_url(self):
        return reverse_lazy('home')


class PostMixin:
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class PostUpdateView(PostMixin, UpdateView):
    template_name = 'women/add_post.html'
    form_class = PostForm
    model = Post

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['post_slug'])

    def get_success_url(self):
        return reverse_lazy('home')


class PostDeleteView(PostMixin, DeleteView):
    template_name = 'women/post_confirm_delete.html'
    model = Post
    slug_url_kwarg = 'post_slug'

    def get_success_url(self):
        return reverse_lazy('home')


class CommentAddView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'women/post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'post_slug': self.kwargs['post_slug']})

    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        new_comment.post = post
        return super().form_valid(new_comment)


class CommentUpdateView(UpdateView):
    template_name = 'women/update_comment.html'
    model = Comment
    form_class = CommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, id=self.kwargs['comment_id'])

    def get_success_url(self):
        post_slug = self.kwargs['post_slug']
        return reverse_lazy('post', kwargs={'post_slug': post_slug})


class CommentDeleteView(DeleteView):
    template_name = 'women/comment_confirm_delete.html'
    model = Comment

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, id=self.kwargs['comment_id'])

    def get_success_url(self):
        post_slug = self.kwargs['post_slug']
        return reverse_lazy('post', kwargs={'post_slug': post_slug})


class CommentAnswerCreateView(CreateView):
    template_name = 'women/update_comment.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        new_comment.post = post
        new_comment.parent = get_object_or_404(Comment, id=self.kwargs['comment_id'])
        return super().form_valid(new_comment)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'post_slug': self.kwargs['post_slug']})


def contact(request):
    return render(request, 'women/contact.html')
