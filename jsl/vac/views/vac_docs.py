from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime
import math


from vac.mymodule import fiscal_year
from vac.forms import *
from vac.models.day_off import DayOff


@login_required
def vac_edit(request, day_off_id=None):
    # return HttpResponse('休暇届編集(新規も)')
    try:
        vacation = Vacation.objects.get(user=request.user, the_year=fiscal_year(datetime.date.today()))
    except Vacation.DoesNotExist:
        vacation = Vacation(user=request.user, the_year=fiscal_year(datetime.date.today()))
        vacation.save()
    # vacation = get_object_or_404(Vacation, user=request.user, the_year=fiscal_year(datetime.date.today()))

    if day_off_id:  # 修正時
        day_off = get_object_or_404(DayOff, pk=day_off_id)

        """JavaScriptで実装済"""
        # day_off.total_days = vacation.transfer_days + vacation.grant_days  # 合計日数は昨年度繰越日数と今年度付与日数を足した値
        # between_days = day_off.end_day - day_off.start_day  # 有給開始と終了の差
        # day_off.used_days = day_off.used_days + between_days.days  # 本年度使用済み日数
        # day_off.rest_days = day_off.total_days - day_off.used_days  # 本年度残り日数
        # if day_off.day_off_type == 70:  # 時間有給の時
        #     used_paid_holiday = day_off.rest_time / 8  # 時間有給残り日数を求める
        #     if day_off.start_time > day_off.end_time:  # 開始時間が終了時間より遅い時
        #         between_time = day_off.start_time.hour - day_off.end_time.hour  # 開始時間と終了時間の差
        #     else:
        #         between_time = day_off.end_time.hour - day_off.start_time.hour  # 開始時間と終了時間の差
        #     day_off.used_time = day_off.used_time - between_time  # 時間有給今年度使用時間
        #     vacation.rest_days = day_off.rest_days - vacation.used_days - used_paid_holiday  # 本年度残り日数

    else:  # 新規時
        day_off = DayOff()
        day_off.apply_day = datetime.date.today()
        day_off.the_year = fiscal_year(day_off.apply_day)
        day_off.user = request.user

    if request.method == 'POST':    # TODO:欠勤の時の動作追加
        form = DayOffForm(request.POST, instance=day_off)
        if form.is_valid():
            between_hour = 0
            if day_off.day_off_type == day_off.DAYOFF_TYPE_LIMIT_PAID_HOLIDAY:
                between_hour = math.floor((datetime.datetime(1970, 1, 1,
                                                             day_off.end_time.hour,
                                                             day_off.end_time.minute,
                                                             day_off.end_time.second) -
                                          datetime.datetime(1970, 1, 1,
                                                            day_off.start_time.hour,
                                                            day_off.start_time.minute,
                                                            day_off.start_time.second)).seconds/3600)
                vacation.used_days = vacation.used_days + math.floor((vacation.used_time + between_hour)/8)  # TODO:下の原因の場所?
                vacation.used_time = vacation.used_time + between_hour
            else:
                between_day = (day_off.end_day - day_off.start_day).days
                vacation.used_days = vacation.used_days + between_day

            vacation.total_days = vacation.transfer_days + vacation.grant_days
            vacation.rest_days = vacation.total_days - vacation.used_days  # TODO:rest_daysが0になってしまう時がある. 原因は上
            if vacation.rest_days < 5:
                vacation.rest_time = vacation.rest_days * 8 - vacation.used_time  # TODO:残り日数が5日を切った時に残り時間の計算が間違っている
            else:
                vacation.rest_time = vacation.rest_time - between_hour  # TODO:rest_timeが正確な値を所持している必要がある
# TODO:修正時の計算を未実装(上記は新規作成時のみ有効です)
            day_off = form.save(commit=False)
            vacation.save()
            day_off.save()
            return redirect('vac:vacation_list')
    else:
        form = DayOffForm(instance=day_off)
    return render(request, 'vac/vac_edit.html', dict(form=form, day_off=day_off,
                                                     day_off_id=day_off_id, vacation=vacation))


@login_required
def vac_del(request, day_off_id=None):
    """休暇届の削除"""
    # day_off = get_object_or_404(DayOff, pk=day_off_id)
    # if day_off.user.employee_id == request.user.employee_id:  # ログインユーザーとdbのユーザー名が一致した時
    day_off = get_object_or_404(DayOff, pk=day_off_id)
    day_off.delete()
    return redirect('vac:vacation_list')
    # else:
    #     HttpResponse('消せません')
    # TODO:削除時にVacationの値も削除前に戻さねばならない

