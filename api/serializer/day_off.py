from rest_framework import serializers

from vac.models import DayOff
from .user import UserSerializer


class DayOffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DayOff
        fields = ('id', 'user', 'day_off_type', 'reason_type', 'detail_type',
                  'apply_day', 'start_day', 'end_day', 'start_time', 'end_time')
