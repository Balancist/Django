from django.db import models
from django.utils import timezone
from Justice.models import User
from django.urls import reverse_lazy

class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='P')


class IP(models.Model):
	ip_address = models.GenericIPAddressField(verbose_name='آی پی')


class Sureh(models.Model):
	name = models.CharField(max_length = 10, verbose_name = 'نام')
	slug = models.SlugField(max_length = 10, verbose_name = 'آدرس')
	number = models.IntegerField(verbose_name = 'شماره')
	discription = models.TextField(verbose_name='توضیحات')

	class Meta:
		verbose_name = 'سوره'
		verbose_name_plural = 'سوره ها'
		ordering = ['number']

	def __str__(self):
		return self.name


class Topic(models.Model):
	name = models.CharField(max_length = 30, verbose_name = 'نام')

	class Meta:
		verbose_name = 'موضوع'
		verbose_name_plural = 'موضوعات'

	def __str__(self):
		return self.name


class Article(models.Model):
	STATUS_CHOICES = (
		('D', 'پیش نویس'),
		('P', 'منتشر شده')
	)
	sureh = models.ForeignKey(Sureh, on_delete = models.CASCADE, verbose_name = 'سوره', related_name='articles')
	ayeh = models.IntegerField(verbose_name = 'آیه')
	topic = models.ManyToManyField(Topic, verbose_name = 'موضوع')
	text = models.TextField(verbose_name = 'متن')
	update = models.DateTimeField(default=timezone.now, verbose_name = 'بروزرسانی')
	status = models.CharField(max_length=1, choices = STATUS_CHOICES, verbose_name = 'وضعیت')
	visit = models.ManyToManyField(IP, through='Visiting', blank=True, verbose_name='بازدید ها', related_name='visits')

	class Meta:
		verbose_name = 'مقاله'
		verbose_name_plural = 'مقالات'

	def topic_to_str(self):
		return ', '.join([topic.name for topic in self.topic.all()])
	topic_to_str.short_description = 'موضوع'

	def __str__(self):
		return self.sureh.name + ' ' + str(self.ayeh)

	objects = ArticleManager()


class Comment(models.Model):
	STATUS_CHOICES = (
		('U', 'تایید نشده'),
		('R', 'رد شده'),
		('C', 'تایید شده')
	)
	article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله', related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
	text = models.TextField(verbose_name='دیدگاه')
	mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دیدگاه مادر', related_name='replies')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U', verbose_name='وضعیت')
	date = models.DateTimeField(auto_now_add=True)
	like = models.IntegerField(default=0, verbose_name='لایک')
	dislike = models.IntegerField(default=0, verbose_name='دیسلایک')

	class Meta:
		verbose_name = 'دیدگاه'
		verbose_name_plural = 'دیدگاه ها'

	def get_absolute_url(self):
		slug = self.article.sureh.slug
		ayeh = self.article.ayeh
		kwargs = {'slug':slug, 'ayeh': ayeh}
		return reverse_lazy('Quran:article', kwargs=kwargs)

	def __str__(self):
		return self.author.get_full_name() + ' | ' + str(self.id)


class Visiting(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	ip = models.ForeignKey(IP, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)