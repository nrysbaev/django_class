from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.all()


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)


class PostCreateView(generic.CreateView):
    template_name = 'blog/add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'
    queryset = models.Post.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class PostUpdateView(generic.UpdateView):
    template_name = 'blog/add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class PostDeleteView(generic.DeleteView):
    template_name = 'blog/post_delete.html'
    success_url = '/posts/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)
