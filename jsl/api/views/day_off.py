from rest_framework import viewsets
from rest_framework.views import APIView

from vac.models import DayOff
from api.serializer import DayOffSerializer


class DayOffViewSet(viewsets.ModelViewSet):
    queryset = DayOff.objects.all()
    serializer_class = DayOffSerializer
