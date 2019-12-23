from rest_framework import serializers


from vac.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('employee_id', 'employee_name')
