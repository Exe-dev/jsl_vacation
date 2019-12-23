from django.test.testcases import TestCase
from vac.core.factories import DayOffFactory, UserFactory, VacationFactory

from vac.models import DayOff


class DayOffTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.day_off = DayOffFactory()
        self.client.login(username=self.user.username, password="password")

    # メニュー画面へのログインテスト
    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # DB登録のテスト
    def test_day_off_add(self):
        response = self.client.get('/day_off/add/')
        self.assertEqual(response.status_code, 200)

        data = {
            'user': self.day_off.user.username,
            'day_off_type': self.day_off.day_off_type,
            'reason_type': self.day_off.reason_type,
            'detail_type': self.day_off.detail_type,
            'apply_day': self.day_off.apply_day,
            'start_day': self.day_off.start_day,
            'end_day': self.day_off.end_day,
            'start_time': self.day_off.start_time,
            'end_time': self.day_off.end_time,
        }

        add = self.client.post('/day_off/add/', data)
        self.assertEqual(add.status_code, 302)

        # データ登録後はリストへリダイレクト

        confirm = DayOff.objects.get(pk=1)
        self.assertEqual(confirm.user.username, data['user'])
        self.assertEqual(confirm.day_off_type, data['day_off_type'])
        self.assertEqual(confirm.reason_type, data['reason_type'])
        self.assertEqual(confirm.detail_type, data['detail_type'])
        self.assertEqual(confirm.apply_day, data['apply_day'])
        self.assertEqual(confirm.start_day, data['start_day'])
        self.assertEqual(confirm.end_day, data['end_day'])
        self.assertEqual(confirm.start_time, data['start_time'])
        self.assertEqual(confirm.end_time, data['end_time'])

    def test_day_off_del(self):
        response = self.client.get('/day_off/del/' + str(self.day_off.id))
        self.assertEqual(response.status_code, 302)

        # データ削除に成功した場合リストへリダイレクト

    def test_day_off_list(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)
