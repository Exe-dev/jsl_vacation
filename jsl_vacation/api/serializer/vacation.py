from rest_framework import serializers


from vac.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ('id', 'the_year', 'user', 'transfer_days', 'grant_days',
                  'total_days', 'used_days', 'used_time', 'rest_days', 'rest_time', 'absence_days')
