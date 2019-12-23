from rest_framework import viewsets

from vac.models import Vacation
from api.serializer import VacationSerializer


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer

vacation_list = VacationViewSet.as_view({
    'get': 'list',
})

vacation_detail = VacationViewSet.as_view({
    'get': 'retrieve',
})