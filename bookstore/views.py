from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'bookstore/book_list.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'bookstore/book_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BookCreateView(generic.CreateView):
    template_name = 'bookstore/book_create.html'
    form_class = forms.BookForm
    success_url = '/books/'
    queryset = models.Book.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = 'bookstore/book_create.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    template_name = 'bookstore/book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


def comment_create(request, id):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect(f'/books/{id}')
    else:
        form = forms.CommentForm()
    return render(request, 'bookstore/comment_create.html', {'form': form})
