# Generated by Django 4.2.2 on 2023-07-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quran', '0003_sureh_discription_alter_article_ayeh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sureh',
            name='discription',
            field=models.TextField(verbose_name='توضیحات'),
        ),
    ]