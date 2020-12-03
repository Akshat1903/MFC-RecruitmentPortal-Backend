# Generated by Django 3.1.3 on 2020-11-29 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('technical_test', models.BooleanField(default=False)),
                ('management_test', models.BooleanField(default=False)),
                ('design_test', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='typeQuestions',
            fields=[
                ('question_id', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('question', models.TextField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_type_questions', to='api.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_responses', to='api.domain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_responses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mcqQuestions',
            fields=[
                ('question_id', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('question', models.TextField()),
                ('option_1', models.CharField(max_length=500)),
                ('option_2', models.CharField(max_length=500)),
                ('option_3', models.CharField(max_length=500)),
                ('option_4', models.CharField(max_length=500)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_mcq_questions', to='api.domain')),
            ],
        ),
    ]