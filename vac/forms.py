from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login
from vac.models import DayOff, Section, User, Vacation


class LoginForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False,
                                                          attrs={'class': 'form-control', 'placeholder': 'Password'}))
    remember = forms.BooleanField(label="Remember me",  help_text="セッションを保存", required=False)

    user = None

    def clean(self):
        if self._errors:
            return
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user:
            if user.is_active:
                self.user = user
            else:
                raise forms.ValidationError('ユーザーは無効です')
        else:
            raise forms.ValidationError('invalid username of password.')
        return self.cleaned_data

    def login(self, request):
        if self.is_valid():
            login(request, self.user)
            if self.cleaned_data['remember']:
                request.session.set_expiry(60 * 60 * 24 * 365 * 5)  # セッションの有効期限を5年とする.
            else:
                request.session.set_expiry(0)  # セッションはブラウザを閉じた時に破棄される
            return True
        return False

    class Meta:
        model = User
        fields = ('username', 'password', )


class DayOffForm(ModelForm):
    """DayOffのフォーム"""
    class Meta:
        model = DayOff
        fields = ('day_off_type', 'reason_type',
                  'detail_type', 'start_day', 'end_day',
                  'start_time', 'end_time', )


class SectionForm(ModelForm):
            """Sectionのフォーム"""
            class Meta:
                model = Section
                fields = ('name', 'order')


class UserForm(ModelForm):
            """Userのフォーム"""

            class Meta:
                model = User
                fields = ('employee_id', 'employee_name', 'section',
                          'regular_entry_date', 'job_entry_date',
                          'continuous_years', 'is_retirement',)


class VacationForm(ModelForm):
            """Vacationのフォーム"""

            class Meta:
                model = Vacation
                fields = ('the_year', 'user', 'transfer_days', 'grant_days',
                          'total_days', 'used_days','used_time',  'rest_days', 'rest_time',
                          'absence_days',)
