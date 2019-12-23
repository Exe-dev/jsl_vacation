from django.db import models


class Vacation(models.Model):
    the_year = models.IntegerField('年度', default=0)
    user = models.ForeignKey('vac.User', verbose_name='ユーザー', related_name='vacations')
    transfer_days = models.IntegerField('繰越日数', default=0)
    grant_days = models.IntegerField('付与日数', default=0)
    total_days = models.IntegerField('合計日数', default=0)
    used_days = models.IntegerField('使用日数', default=0)
    used_time = models.IntegerField('使用時間', default=0)
    rest_days = models.IntegerField('残日数', default=0)
    rest_time = models.IntegerField('残時間', default=40)
    absence_days = models.IntegerField('欠勤日数', default=0)

    # def __str__(self):
    #     return self.name

