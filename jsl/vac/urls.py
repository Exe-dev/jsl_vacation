from django.conf.urls import url
from django.contrib.auth import views

from vac.views import list, menu, vac_docs, login, pulldown

urlpatterns = [
    # 休暇一覧表示
    url(r'^list/$', list.DayOffListView.as_view(), name='vacation_list'),
    # メニュー
    url(r'^$', menu.menu, name='vacation_menu'),
    # 新規休暇届
    url(r'^day_off/add/$', vac_docs.vac_edit, name='day_off_add'),
    # 休暇届修正
    url(r'^day_off/edit/(?P<day_off_id>\d+)$', vac_docs.vac_edit, name='day_off_edit'),
    # 休暇届削除
    url(r'^day_off/del/(?P<day_off_id>\d+)$', vac_docs.vac_del, name='day_off_del'),
    # ログイン
    url(r'^login/$', login.login_view, name='login'),
    # ログアウト
    url(r'^logout/$', views.logout_then_login, name='logout'),
    # プルダウンの動的変更
    url(r'^pulldown/(?P<type>\w+)/(?P<select_id>\d+)/(?P<next_id>\d+)', pulldown.pulldown, name='pulldown'),
]
