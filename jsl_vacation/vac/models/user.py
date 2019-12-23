from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    employee_id = models.CharField('社員番号', unique=True, max_length=255, blank=True, null=True)
    employee_name = models.CharField('氏名', max_length=255, blank=True, null=True)
    employee_kana = models.CharField('氏名(カナ)', max_length=255, blank=True, null=True)
    section = models.ForeignKey('vac.Section', verbose_name='所属', related_name='users', blank=True, null=True)
    regular_entry_date = models.DateField('正規の入社年月日', blank=True, null=True)
    job_entry_date = models.DateField('入社年月日', blank=True, null=True)
    continuous_years = models.IntegerField('勤続年数', blank=True, null=True)
    is_retirement = models.BooleanField('退職フラグ', default=False)

    def __str__(self):
        return self.username
