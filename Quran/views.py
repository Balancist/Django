from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .mixins import FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sureh, Article, Comment
from .forms import CommentForm

class Index(ListView):
	template_name = 'quran/index.html'
	model = Sureh


class SurehDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Sureh, slug=slug)
	template_name = 'quran/sureh.html'


class ArticleDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		ayeh = self.kwargs.get('ayeh')
		article = get_object_or_404(Article.objects.published(), sureh__slug=slug, ayeh=ayeh)
		ip_address = self.request.user.ip_address
		if ip_address not in article.visit.all():
			article.visit.add(ip_address)
		return article
	template_name = 'quran/article.html'


class AddComment(LoginRequiredMixin, FormValidMixin, CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'quran/article.html'

class EditComment(AuthorAccessMixin, UpdateView):
	model = Comment
	fields = ['text']
	template_name = 'quran/comments.html'


class DeleteComment(AuthorAccessMixin, DeleteView):
	model = Comment
	success_url = reverse_lazy('Quran:article')