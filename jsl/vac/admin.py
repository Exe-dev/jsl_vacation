from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _


from .models import DayOff, User, Vacation, Section


class VacationAdmin(admin.ModelAdmin):
    list_display = ('the_year', 'user', 'transfer_days', 'grant_days',
                    'total_days', 'used_days', 'rest_days', 'rest_time',
                    'absence_days',) # 一覧に出したい項目
    # list_display_links = ('', '',)  # 修正リンクでクリックできる項目
admin.site.register(Vacation, VacationAdmin)


class UserAdmin(BaseUserAdmin):
        list_display = ('employee_id', 'employee_name',  'section',
                        'regular_entry_date', 'job_entry_date',
                        'continuous_years', 'is_retirement',
                        )# 一覧に出したい項目
        fieldsets = (
            (None, {'fields': ('username', 'password')}),
            (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                           'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            ('社員プロファイル', {'fields': ('employee_id', 'employee_name',  'section',
                        'regular_entry_date', 'job_entry_date',
                        'continuous_years', 'is_retirement',)}),
        )
        # list_display_links = ('', '',)  # 修正リンクでクリックできる項目
admin.site.register(User, UserAdmin)


class DayOffAdmin(admin.ModelAdmin):
    list_display = ('the_year', 'user', 'day_off_type', 'reason_type',
                    'detail_type', 'apply_day', 'start_day', 'end_day',
                    'start_time', 'end_time', 'working_holiday',
                    'compensatory_holiday', 'transfer_day', 'working_day',
                    'vacation_days', 'total_days', 'total_time', 'used_days',
                    'used_time', 'rest_days', 'rest_time',)# 一覧に出したい項目
    # list_display_links = ('', '',)  # 修正リンクでクリックできる項目
admin.site.register(DayOff,DayOffAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',) # 一覧に出したい項目
    # list_display_links = ('', '',)  # 修正リンクでクリックできる項目
admin.site.register(Section, SectionAdmin)


