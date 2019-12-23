# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 01:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='社員番号')),
                ('employee_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='氏名')),
                ('employee_kana', models.CharField(blank=True, max_length=255, null=True, verbose_name='氏名(カナ)')),
                ('regular_entry_date', models.DateField(blank=True, null=True, verbose_name='正規の入社年月日')),
                ('job_entry_date', models.DateField(blank=True, null=True, verbose_name='入社年月日')),
                ('continuous_years', models.IntegerField(blank=True, null=True, verbose_name='勤続年数')),
                ('is_retirement', models.BooleanField(default=False, verbose_name='退職フラグ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DayOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_year', models.IntegerField(verbose_name='年度')),
                ('day_off_type', models.IntegerField(choices=[(10, '有給休暇'), (20, '半日休暇(午前)'), (30, '半日休暇(午後)'), (40, '特別休暇'), (50, '欠勤'), (60, '半日欠勤'), (70, '時間制限有給休暇')], null=True, verbose_name='区分')),
                ('reason_type', models.IntegerField(choices=[(10, '病気'), (20, '家事都合'), (30, '慶事'), (40, '弔事'), (50, 'その他')], null=True, verbose_name='事由')),
                ('detail_type', models.IntegerField(blank=True, choices=[(10, '本人が結婚'), (20, '本人の子供が結婚'), (30, '配偶者の出産'), (40, '弔事(配偶者・実父母・実養子・祖父母・配偶者の父母・兄弟姉妹・孫)')], default=None, null=True, verbose_name='事由・詳細')),
                ('apply_day', models.DateField(null=True, verbose_name='届出日')),
                ('start_day', models.DateField(blank=True, null=True, verbose_name='開始日')),
                ('end_day', models.DateField(blank=True, null=True, verbose_name='終了日')),
                ('start_time', models.TimeField(blank=True, choices=[(datetime.time(8, 30), '8:30'), (datetime.time(9, 0), '9:00'), (datetime.time(9, 30), '9:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30')], null=True, verbose_name='開始時間')),
                ('end_time', models.TimeField(blank=True, choices=[(datetime.time(8, 30), '8:30'), (datetime.time(9, 0), '9:00'), (datetime.time(9, 30), '9:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30')], null=True, verbose_name='終了時間')),
                ('working_holiday', models.DateField(blank=True, null=True, verbose_name='休出日')),
                ('compensatory_holiday', models.DateField(blank=True, null=True, verbose_name='代休日')),
                ('transfer_day', models.DateField(blank=True, null=True, verbose_name='振替日')),
                ('working_day', models.DateField(blank=True, null=True, verbose_name='出勤日')),
                ('vacation_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='休暇日数')),
                ('total_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='合計日数')),
                ('total_time', models.IntegerField(blank=True, default=0, null=True, verbose_name='合計時間')),
                ('used_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='使用日数')),
                ('used_time', models.IntegerField(blank=True, default=0, null=True, verbose_name='使用時間')),
                ('rest_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='残日数')),
                ('rest_time', models.IntegerField(blank=True, default=40, null=True, verbose_name='残時間')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='コメント')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vac', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='所属名')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='ソート順')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_year', models.IntegerField(default=0, verbose_name='年度')),
                ('transfer_days', models.IntegerField(default=0, verbose_name='繰越日数')),
                ('grant_days', models.IntegerField(default=0, verbose_name='付与日数')),
                ('total_days', models.IntegerField(default=0, verbose_name='合計日数')),
                ('used_days', models.IntegerField(default=0, verbose_name='使用日数')),
                ('used_time', models.IntegerField(default=0, verbose_name='使用時間')),
                ('rest_days', models.IntegerField(default=0, verbose_name='残日数')),
                ('rest_time', models.IntegerField(default=40, verbose_name='残時間')),
                ('absence_days', models.IntegerField(default=0, verbose_name='欠勤日数')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacations', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='vac.Section', verbose_name='所属'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
