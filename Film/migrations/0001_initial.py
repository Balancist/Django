# Generated by Django 4.2.2 on 2023-07-16 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('slug', models.SlugField(max_length=30, verbose_name='آدرس')),
                ('chapter', models.IntegerField(default=0, verbose_name='تعداد قسمت ها')),
            ],
            options={
                'verbose_name': 'مجموعه',
                'verbose_name_plural': 'مجموعه ها',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('slug', models.SlugField(max_length=30, verbose_name='آدرس')),
                ('founder', models.CharField(max_length=50, verbose_name='موسس')),
                ('antiquity', models.IntegerField(default=0, verbose_name='قدمت')),
                ('logo', models.ImageField(upload_to='image/film/company', verbose_name='آرم')),
            ],
            options={
                'verbose_name': 'شرکت',
                'verbose_name_plural': 'شرکت ها',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('slug', models.SlugField(max_length=30, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'ژانر',
                'verbose_name_plural': 'ژانر ها',
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('slug', models.SlugField(max_length=30, verbose_name='آدرس')),
                ('founder', models.CharField(max_length=50, verbose_name='موسس')),
                ('antiquity', models.IntegerField(default=0, verbose_name='قدمت')),
                ('logo', models.ImageField(upload_to='image/film/stream', verbose_name='آرم')),
            ],
            options={
                'verbose_name': 'پخش کننده',
                'verbose_name_plural': 'پخش کننده ها',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='آدرس')),
                ('kind', models.CharField(choices=[('M', 'سریال'), ('A', 'انیمیشن')], max_length=1, verbose_name='نوع')),
                ('season', models.IntegerField(default=0, verbose_name='تعداد فصول')),
                ('status', models.CharField(choices=[('P', 'در حال انتشار'), ('E', 'پایان یافته')], max_length=1, verbose_name='وضعیت')),
                ('poster', models.ImageField(upload_to='image/film/serie', verbose_name='پوستر')),
                ('company', models.ManyToManyField(to='Film.company', verbose_name='شرکت')),
                ('genre', models.ManyToManyField(to='Film.genre', verbose_name='ژانر')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Film.stream', verbose_name='پخش کننده')),
            ],
            options={
                'verbose_name': 'سریال',
                'verbose_name_plural': 'سریال ها',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='آدرس')),
                ('year', models.IntegerField(default=0, verbose_name='سال')),
                ('kind', models.CharField(choices=[('M', 'سینمایی'), ('C', 'کارتون')], max_length=1, verbose_name='نوع')),
                ('chapter', models.IntegerField(null=True, verbose_name='شماره قسمت')),
                ('poster', models.ImageField(upload_to='image/film/film', verbose_name='پوستر')),
                ('video', models.FileField(upload_to='video/film/film', verbose_name='ویدیو')),
                ('download', models.CharField(max_length=1000, verbose_name='لینک')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Film.collection', verbose_name='مجموعه')),
                ('company', models.ManyToManyField(to='Film.company', verbose_name='شرکت')),
                ('genre', models.ManyToManyField(to='Film.genre', verbose_name='ژانر')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم ها',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='آدرس')),
                ('video', models.FileField(upload_to='video/film/serie', verbose_name='ویدیو')),
                ('download', models.CharField(max_length=1000, verbose_name='لینک')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Film.serie', verbose_name='سریال')),
            ],
            options={
                'verbose_name': 'قسمت',
                'verbose_name_plural': 'قسمت ها',
            },
        ),
    ]
