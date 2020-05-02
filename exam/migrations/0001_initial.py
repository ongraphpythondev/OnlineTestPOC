# Generated by Django 3.0.5 on 2020-04-22 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('duration', models.DurationField()),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
                ('examinee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=8)),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='exam.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exam.Option')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='exam.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exam.Test')),
            ],
        ),
    ]
