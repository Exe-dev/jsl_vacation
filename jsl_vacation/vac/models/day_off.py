from django.db import models
from datetime import time


from vac.models.vacation import Vacation


class DayOff(models.Model):

    DAYOFF_TYPE_PAID_HOLIDAY = 10
    DAYOFF_TYPE_HALF_PAID_HOLIDAY_AM = 20
    DAYOFF_TYPE_HALF_PAID_HOLIDAY_PM = 30
    DAYOFF_TYPE_SPECIAL = 40
    DAYOFF_TYPE_ABSENCE = 50
    DAYOFF_TYPE_HALF_ABSENCE = 60
    DAYOFF_TYPE_LIMIT_PAID_HOLIDAY = 70

    REASON_TYPE_SICK = 10
    REASON_TYPE_HOUSE_WORK = 20
    REASON_TYPE_AUSPICIOUS = 30
    REASON_TYPE_CONDOLENCE = 40
    REASON_TYPE_OTHER = 50

    DETAIL_TYPE_MARRY = 10
    DETAIL_TYPE_MARRY_CHILD = 20
    DETAIL_TYPE_BIRTH = 30
    DETAIL_TYPE_CONDOLENCE = 40

    DAYOFF_TYPE_CHOICE = (
        (DAYOFF_TYPE_PAID_HOLIDAY, "有給休暇"),
        (DAYOFF_TYPE_HALF_PAID_HOLIDAY_AM, "半日休暇(午前)"),
        (DAYOFF_TYPE_HALF_PAID_HOLIDAY_PM, "半日休暇(午後)"),
        (DAYOFF_TYPE_SPECIAL, "特別休暇"),
        (DAYOFF_TYPE_ABSENCE, "欠勤"),
        (DAYOFF_TYPE_HALF_ABSENCE, "半日欠勤"),
        (DAYOFF_TYPE_LIMIT_PAID_HOLIDAY, "時間制限有給休暇"),
    )

    REASON_TYPE_CHOICE = (
        (REASON_TYPE_SICK, "病気"),  # 有給など
        (REASON_TYPE_HOUSE_WORK, "家事都合"),  # 有給など
        (REASON_TYPE_AUSPICIOUS, "慶事"),  # 特別休暇
        (REASON_TYPE_CONDOLENCE, "弔事"),  # 特別休暇
        (REASON_TYPE_OTHER, "その他"),
    )

    DETAIL_TYPE_CHOICE = (
        (DETAIL_TYPE_MARRY, "本人が結婚"),  # 慶事・弔事
        (DETAIL_TYPE_MARRY_CHILD, "本人の子供が結婚"),  # 慶事・弔事
        (DETAIL_TYPE_BIRTH, "配偶者の出産"),  # 慶事・弔事
        (DETAIL_TYPE_CONDOLENCE, "弔事(配偶者・実父母・実養子・祖父母・配偶者の父母・兄弟姉妹・孫)"),  # 弔事
    )

    TIME_CHOICE = (
        (time(8, 30, 00), "8:30"),
        (time(9, 00, 00), "9:00"),
        (time(9, 30, 00), "9:30"),
        (time(10, 00, 00), "10:00"),
        (time(10, 30, 00), "10:30"),
        (time(11, 00, 00), "11:00"),
        (time(11, 30, 00), "11:30"),
        (time(12, 00, 00), "12:00"),
        (time(12, 30, 00), "12:30"),
        (time(13, 00, 00), "13:00"),
        (time(13, 30, 00), "13:30"),
        (time(14, 00, 00), "14:00"),
        (time(14, 30, 00), "14:30"),
        (time(15, 00, 00), "15:00"),
        (time(15, 30, 00), "15:30"),
        (time(16, 00, 00), "16:00"),
        (time(16, 30, 00), "16:30"),
        (time(17, 00, 00), "17:00"),
        (time(17, 30, 00), "17:30"),
    )

    the_year = models.IntegerField('年度')
    user = models.ForeignKey('vac.User', verbose_name='ユーザー', related_name='vac')

    day_off_type = models.IntegerField('区分', blank=False, null=True, choices=DAYOFF_TYPE_CHOICE)
    reason_type = models.IntegerField('事由', blank=False, null=True, choices=REASON_TYPE_CHOICE)
    detail_type = models.IntegerField('事由・詳細', blank=True, null=True, default=None, choices=DETAIL_TYPE_CHOICE)

    apply_day = models.DateField('届出日', blank=False, null=True)
    start_day = models.DateField('開始日', blank=True, null=True)
    end_day = models.DateField('終了日', blank=True, null=True)
    start_time = models.TimeField('開始時間', blank=True, null=True, choices=TIME_CHOICE)
    end_time = models.TimeField('終了時間', blank=True, null=True, choices=TIME_CHOICE)

    working_holiday = models.DateField('休出日', blank=True, null=True)
    compensatory_holiday = models.DateField('代休日', blank=True, null=True)
    transfer_day = models.DateField('振替日', blank=True, null=True)
    working_day = models.DateField('出勤日', blank=True, null=True)
    vacation_days = models.IntegerField('休暇日数', blank=True, null=True, default=0)
    total_days = models.IntegerField('合計日数', blank=True, null=True, default=0)
    total_time = models.IntegerField('合計時間', blank=True, null=True, default=0)
    used_days = models.IntegerField('使用日数', blank=True, null=True, default=0)
    used_time = models.IntegerField('使用時間', blank=True, null=True, default=0)
    rest_days = models.IntegerField('残日数', blank=True, null=True, default=0)
    rest_time = models.IntegerField('残時間', blank=True, null=True, default=40)

    comment = models.TextField('コメント', blank=True, null=True)

    def __str__(self):
        return self.user.username if self.user else ''

    # @classmethod
    # def day_off_type(cls, day_off_type):
    #     if day_off_type in [
    #                         cls.DAYOFF_TYPE_PAID_HOLIDAY,
    #                         cls.DAYOFF_TYPE_HALF_PAID_HOLIDAY_AM,
    #                         cls.DAYOFF_TYPE_HALF_PAID_HOLIDAY_PM,
    #                         cls.DAYOFF_TYPE_ABSENCE,
    #                         cls.DAYOFF_TYPE_HALF_ABSENCE,
    #                         cls.DAYOFF_TYPE_LIMIT_PAID_HOLIDAY,
    #                         ]:#有給休暇、半日有給(午前)、半日有給(午後)、欠勤、半日欠勤、時間指定有給休暇の場合
    #         return [
    #                 cls.REASON_TYPE_SICK,
    #                 cls.REASON_TYPE_HOUSE_WORK,
    #                 cls.REASON_TYPE_OTHER
    #                 ]
    #     elif day_off_type == cls.DAYOFF_TYPE_SPECIAL:#特別休暇の場合
    #         return [cls.REASON_TYPE_AUSPICIOUS,
    #                 cls.REASON_TYPE_CONDOLENCE,
    #                 cls.REASON_TYPE_OTHER,]
    #
    #
    # def get_reason_type(cls, reason_type):
    #      if reason_type in [
    #          cls.REASON_TYPE_AUSPICIOUS,
    #          cls.REASON_TYPE_CONDOLENCE,
    #      ]:#理由が慶次か弔辞の場合
    #          return [
    #          cls.DETAIL_TYPE_MARRY,
    #          cls.DETAIL_TYPE_MARRY_CHILD,
    #          cls. DETAIL_TYPE_BIRTH,
    #          ]
    #      elif reason_type== cls._TYPE_CONDOLENCE:#弔辞の場合
    #          return[
    #              cls.DETAIL_TYPE_CONDOLENCE
    #          ]
    #      else:#それ以外の場合
    #          return



    # def clean(self):
    #     reason_clean = self.cleaned_data.get(DayOff.day_off_type)
    #     detail_clean = self.cleaned_data.get(DayOff.reason_type)