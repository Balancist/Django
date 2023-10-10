from django.db import models
from django.utils.html import format_html

class Company(models.Model):
	name = models.CharField(max_length=30, verbose_name='نام')
	slug = models.SlugField(max_length=30, verbose_name='آدرس')
	mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='شرکت مادر', related_name='children')
	year = models.IntegerField(default=0, verbose_name='سال تاسیس')
	logo = models.ImageField(upload_to='image/film/company', verbose_name='آرم')
	
	class Meta:
		verbose_name = 'شرکت'
		verbose_name_plural = 'شرکت ها'

	def logo_tag(self):
		return format_html("<img src='{}' width=100 height=50 style='border-radius:5px'>".format(self.logo.url))
	logo_tag.short_description = 'آرم'

	def __str__(self):
		return self.name


class Stream(models.Model):
	name = models.CharField(max_length=30, verbose_name='نام')
	slug = models.SlugField(max_length=30, verbose_name='آدرس')
	year = models.IntegerField(default=0, verbose_name='سال تاسیس')
	logo = models.ImageField(upload_to='image/film/stream', verbose_name='آرم')
	
	class Meta:
		verbose_name = 'پخش کننده'
		verbose_name_plural = 'پخش کننده ها'

	def logo_tag(self):
		return format_html("<img src='{}' width=100 height=50 style='border-radius:5px'>".format(self.logo.url))
	logo_tag.short_description = 'آرم'

	def __str__(self):
		return self.name


class Genre(models.Model):
	name = models.CharField(max_length=30, verbose_name='نام')
	slug = models.SlugField(max_length=30, verbose_name='آدرس')

	class Meta:
		verbose_name = 'ژانر'
		verbose_name_plural = 'ژانر ها'

	def __str__(self):
		return self.name


class Collection(models.Model):
	STATUS_CHOICES = (
		('P', 'در حال پخش'),
		('B', 'در حال ساخت'),
		('E', 'پایان یافته'),
		('U', 'نا معلوم')
	)
	name = models.CharField(max_length=100, verbose_name='نام')
	slug = models.SlugField(max_length=30, verbose_name='آدرس')
	chapter = models.IntegerField(default=0, verbose_name='تعداد قسمت ها')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U', verbose_name='وضعیت')

	class Meta:
		verbose_name = 'مجموعه'
		verbose_name_plural = 'مجموعه ها'

	def __str__(self):
		return self.name


class Film(models.Model):
	KIND_CHOICES = (
		('M', 'سینمایی'),
		('C', 'کارتون')
	)
	title = models.CharField(max_length=100, verbose_name='عنوان')
	slug = models.SlugField(verbose_name='آدرس')
	year = models.IntegerField(default=0, verbose_name='سال')
	kind = models.CharField(max_length=1, choices=KIND_CHOICES, verbose_name='نوع')
	genre = models.ManyToManyField(Genre, verbose_name='ژانر', related_name='films')
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True, verbose_name='مجموعه')
	chapter = models.IntegerField(null=True, verbose_name='شماره قسمت')
	company = models.ManyToManyField(Company, verbose_name='شرکت', related_name='films')
	poster = models.ImageField(upload_to='image/film/film', verbose_name='پوستر')
	video = models.FileField(upload_to='video/film/film', verbose_name='ویدیو')
	download = models.CharField(max_length=1000, verbose_name='لینک')

	class Meta:
		verbose_name = 'فیلم'
		verbose_name_plural = 'فیلم ها'

	def genre_to_str(self):
		return ' | '.join([genre.name for genre in self.genre.all()])
	genre_to_str.short_description = 'ژانر'

	def company_to_str(self):
		return ' | '.join([company.name for company in self.company.all()])
	company_to_str.short_description = 'شرکت'

	def poster_tag(self):
		return format_html("<img src='{}' width=70 height=100 style='border-radius:5px'>".format(self.poster.url))
	poster_tag.short_description = 'پوستر'

	def __str__(self):
		return self.title


class Serie(models.Model):
	KIND_CHOICES = (
		('M', 'سریال'),
		('A', 'انیمیشن')
	)
	STATUS_CHOICES = (
		('P', 'در حال پخش'),
		('B', 'در حال ساخت'),
		('E', 'پایان یافته'),
		('U', 'نا معلوم')
	)
	title = models.CharField(max_length=100, verbose_name='عنوان')
	slug = models.SlugField(verbose_name='آدرس')
	kind = models.CharField(max_length=1, choices=KIND_CHOICES, verbose_name='نوع')
	genre = models.ManyToManyField(Genre, verbose_name='ژانر', related_name='series')
	first = models.IntegerField(default=0, verbose_name='اولین انتشار')
	last = models.IntegerField(default=0, verbose_name='آخرین انتشار')
	season = models.IntegerField(default=0, verbose_name='تعداد فصول')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
	company = models.ManyToManyField(Company, verbose_name='شرکت', related_name='series')
	stream = models.ForeignKey(Stream, on_delete=models.CASCADE, verbose_name='پخش کننده')
	poster = models.ImageField(upload_to='image/film/serie', verbose_name='پوستر')

	class Meta:
		verbose_name = 'سریال'
		verbose_name_plural = 'سریال ها'

	def genre_to_str(self):
		return ' | '.join([genre.name for genre in self.genre.all()])
	genre_to_str.short_description = 'ژانر'

	def company_to_str(self):
		return ' | '.join([company.name for company in self.company.all()])
	company_to_str.short_description = 'شرکت'

	def poster_tag(self):
		return format_html("<img src='{}' width=70 height=100 style='border-radius:5px'>".format(self.poster.url))
	poster_tag.short_description = 'پوستر'

	def __str__(self):
		return self.title


class Episode(models.Model):
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name='سریال')
	slug = models.SlugField(verbose_name='آدرس')
	video = models.FileField(upload_to='video/film/serie', verbose_name='ویدیو')
	download = models.CharField(max_length=1000, verbose_name='لینک')
	size = models.IntegerField(default=0, verbose_name='حجم')


	class Meta:
		verbose_name = 'قسمت'
		verbose_name_plural = 'قسمت ها'

	def __str__(self):
		return self.slug