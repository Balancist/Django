from django import template
from ..forms import CommentForm
from ..models import Article
from django.db.models import Count, Q
from datetime import datetime, timedelta

register = template.Library()

@register.inclusion_tag('quran/comments.html')
def comment(article):
	return {
	'form': CommentForm,
	'comments': article.comments.all(),
	'article': article
	}

@register.inclusion_tag('quran/popular.html')
def popular():
	recent_week = datetime.today() - timedelta(days=7)
	return {
	'list': Article.objects.published().annotate(count=Count('visit', filter=Q(visiting__date__gt=recent_week))).order_by('-count', '-pk')[:5]
	}

@register.inclusion_tag('quran/hot.html')
def hot():
	recent_week = datetime.today() - timedelta(days=7)
	return {
	'list': Article.objects.published().annotate(count=Count('comments', filter=Q(comments__date__gt=recent_week))).order_by('-count', '-pk')[:5]
	}