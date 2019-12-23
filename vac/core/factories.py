import factory
from factory import fuzzy
from django.contrib.auth import get_user_model
from vac.models import DayOff, Vacation
from datetime import date, time

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')

    employee_id = factory.Sequence(lambda n: n)
    employee_name = factory.Sequence(lambda n: 'employee_{0}'.format(n))

    regular_entry_date = date(2017, 1, 1)
    job_entry_date = date(2017, 2, 1)


class DayOffFactory(factory.DjangoModelFactory):
    class Meta:
        model = DayOff

    the_year = 2017
    user = factory.SubFactory(UserFactory)

    day_off_type = fuzzy.FuzzyChoice(choices=list(map(lambda n: n[0], DayOff.DAYOFF_TYPE_CHOICE)))
    reason_type = fuzzy.FuzzyChoice(choices=list(map(lambda n: n[0], DayOff.REASON_TYPE_CHOICE)))
    detail_type = fuzzy.FuzzyChoice(choices=list(map(lambda n: n[0], DayOff.DETAIL_TYPE_CHOICE)))

    apply_day = date(2017, 1, 1)
    start_day = date(2017, 9, 4)
    end_day = date(2017, 9, 15)
    start_time = time(8, 30, 00)
    end_time = time(17, 30, 00)


class VacationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vacation

    user = factory.SubFactory(UserFactory)
    transfer_days = 0
    total_days = 0
    used_days = 0
    used_time = 0
    rest_days = 0
    rest_time = 40
    absence_days = 0