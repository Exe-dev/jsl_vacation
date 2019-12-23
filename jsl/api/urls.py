from rest_framework import routers
from django.conf.urls import url
from .views import DayOffViewSet
from .views import vacation_detail, vacation_list
from .views import user_list, user_detail

day_off_list = DayOffViewSet.as_view({
    'get': 'list',
})
day_off_detail = DayOffViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    url(r'^users/$', user_list, name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user_list'),
    url(r'^day_offs/$', day_off_list, name='day_off_list'),
    url(r'^day_offs/(?P<pk>\d+)/$', day_off_detail, name='day_off_detail'),
    url(r'^vacations/$', vacation_list, name='vacation_list'),
    url(r'^vacations/(?P<pk>[0-9]+)/$', vacation_detail, name='vacation-detail')
]

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'dayoff', DayOffViewSet)
