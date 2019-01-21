# Generated by Django 2.1.5 on 2019-01-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='a_tag',
            new_name='a_desc',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='a_id',
            new_name='cate',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='a_icon',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='a_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='a_content',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='is_open',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='c_desc',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='c_keyword',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='p_node',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='c_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
