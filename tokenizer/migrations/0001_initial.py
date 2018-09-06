# Generated by Django 2.1.1 on 2018-09-06 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2048, verbose_name='Ссылка')),
                ('token', models.CharField(help_text='Сокращенная ссылка', max_length=16)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('redirect_count', models.IntegerField(verbose_name='Количество переходов по ссылке')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
