from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
	first_name = models.CharField(max_length=50, verbose_name='نام')
	last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
	phone_number = PhoneNumberField(unique=True, verbose_name='شماره تلفن')
	is_valid = models.BooleanField(default=False, verbose_name='اعتبار سنجی')


class Crime(models.Model):
	name = models.CharField(max_length=100, verbose_name='نام')
	slug = models.SlugField(verbose_name='آدرس')
	field = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='زمینه', related_name='subfields')
	law = models.TextField(verbose_name='قانون')

	class Meta:
		verbose_name = 'جرم'
		verbose_name_plural = 'جرم ها'
		ordering = ['name']

	def __str__(self):
		return self.name


class Culprit(models.Model):
	first_name = models.CharField(max_length=50, blank=True, verbose_name='اسم')
	last_name = models.CharField(max_length=50, blank=True, verbose_name='فامیلی')
	#nick_name = models.ListField()
	instagram_id = models.SlugField(blank=True, verbose_name='آیدی اینستاگرام')
	telegram_id = models.SlugField(blank=True, verbose_name='آیدی تلگرام')
	twitter_id = models.SlugField(blank=True, verbose_name='آیدی توییتر')
	rubika_id = models.SlugField(blank=True, verbose_name='آیدی روبیکا')
	#phone_number = ListField()
	face = models.TextField(verbose_name='مشخصات چهره')
	height = models.IntegerField(null=True, verbose_name='قد')
	weight = models.IntegerField(null=True, verbose_name='وزن')
	body = models.TextField(verbose_name='مشخصات بدنی دیگر')
	#weapon = models.ListField()
	job = models.CharField(blank=True, max_length=500, verbose_name='شغل')
	#location = models.LocationField()
	address = models.CharField(blank=True, max_length=5000, verbose_name='آدرس')
	video = models.FileField(upload_to='video/justice/culprit', blank=True, verbose_name='ویدیو')
	v_caption = models.TextField(blank=True, verbose_name='توضیحات ویدیو')
	audio = models.FileField(upload_to='audio/justice/culprit', blank=True, verbose_name='صدا')
	a_caption = models.TextField(blank=True, verbose_name='توضیحات صدا')
	picture = models.ImageField(upload_to='image/justice/culprit', blank=True, verbose_name='عکس')
	p_caption = models.TextField(blank=True, verbose_name='توضیحات عکس')

	class Meta:
		verbose_name = 'مجرم'
		verbose_name_plural = 'مجرمین'
		ordering = ['last_name', 'first_name']

	def __str__(self):
		first_name = self.first_name
		last_name = self.last_name
		x = first_name and last_name
		if x:
			return first_name + ' ' + last_name
		else:
			return 'ناشناس-' + str(self.id)
	

class Complaint(models.Model):
	URGENCY_CHOICES = (
		('A', 'آنی: جرم در حال وقوع است'),
		('F', 'فوری: جرم بزودی تکرار می شود'),
		('Q', 'غیر فوری: جرم انجام شده و شکایت برای احقاق حق است')
	)
	STATUS_CHOICES = (
		('Y', 'رسیدگی شده'),
		('I', 'در حال رسیدگی'),
		('L', 'در صف رسیدگی'),
		('N', 'بررسی نشده')
	)
	crime = models.ManyToManyField(Crime, verbose_name='جرم', related_name='complaints')
	complainant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='شاکی', related_name='complaints')
	urgency = models.CharField(max_length=1, choices=URGENCY_CHOICES, verbose_name='فوریت')
	date = models.DateTimeField(default=timezone.now, verbose_name='زمان وقوع')
	discription = models.TextField(blank=True, verbose_name='توضیح دلیل شکایت')
	#location = models.LocationField()
	culprit = models.ManyToManyField(Culprit, verbose_name='مجرم', related_name='complaints')
	video = models.FileField(upload_to='video/justice/complaint', blank=True, verbose_name='ویدیو')
	v_caption = models.TextField(blank=True, verbose_name='توضیحات ویدیو')
	audio = models.FileField(upload_to='audio/justice/complaint', blank=True, verbose_name='صدا')
	a_caption = models.TextField(blank=True, verbose_name='توضیحات صدا')
	picture = models.ImageField(upload_to='image/justice/complaint', blank=True, verbose_name='عکس')
	p_caption = models.TextField(blank=True, verbose_name='توضیحات عکس')
	filed = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N', verbose_name='وضعیت شکایت')

	class Meta:
		verbose_name = 'شکایت'
		verbose_name_plural = 'شکایات'
		ordering = ['id']

	def get_absolute_url(self):
		return reverse('Justice:profile')

	def crime_to_str(self):
		return ' | '.join([crime.name for crime in self.crime.all()])
	crime_to_str.short_description = 'جرم'

	def culprit_to_str(self):
		return ' | '.join([culprit.first_name + ' ' + culprit.last_name for culprit in self.culprit.all()])
	culprit_to_str.short_description = 'مجرم'

	def __str__(self):
		return str(self.id)