from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Comment, Article

class FormValidMixin():
    def dispatch(self, request, slug, ayeh, *args, **kwargs):
        global article
        article = get_object_or_404(Article.objects.published(), sureh__slug=slug, ayeh=ayeh)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.article = article
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author == request.user:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404()


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()