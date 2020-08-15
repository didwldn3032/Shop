# Generated by Django 3.1 on 2020-08-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200810_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='_type',
            field=models.PositiveSmallIntegerField(choices=[('F', '여성'), ('M', '남성')], null=True, verbose_name='게시글타입'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='상세보기'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성시간'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='상품사진'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.TextField(null=True, verbose_name='가격'),
        ),
        migrations.AlterField(
            model_name='post',
            name='remaining',
            field=models.TextField(null=True, verbose_name='재고'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='상품명'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정시간'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='조회수'),
        ),
    ]