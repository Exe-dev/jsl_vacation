from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from vac.models.day_off import DayOff


@method_decorator(login_required, name='dispatch')
class DayOffListView(ListView):
    context_object_name = 'day_offs'
    template_name = 'vac/vac_list.html'
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        the_year = request.GET.get('the_year', '')
        user_employee_id = request.GET.get('user_employee_id', '')
        day_offs = DayOff.objects.select_related('user').all()
        if the_year:
            day_offs = day_offs.filter(the_year=the_year)
        if user_employee_id:
            day_offs = day_offs.filter(user__employee_id=user_employee_id)
        day_offs = day_offs.order_by('-id')
        self.object_list = day_offs

        context = self.get_context_data(object_list=self.object_list,
                                        the_year=the_year,
                                        user_employee_id=user_employee_id)
        return self.render_to_response(context)
