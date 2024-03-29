# Generated by Django 2.1.5 on 2019-02-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_categories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='Name',
            field=models.CharField(default='John', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='post',
            name='Category',
        ),
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ManyToManyField(to='blog.Categories'),
        ),
    ]
