from django.http import HttpResponse
from django.shortcuts import redirect

from vac.models import DayOff


def pulldown(request, type, select_id, next_id):
    select_id = int(select_id)
    reason = DayOff.REASON_TYPE_CHOICE
    detail = DayOff.DETAIL_TYPE_CHOICE
    remarks = []
    if type == "dayoff":
        if select_id in {DayOff.DAYOFF_TYPE_PAID_HOLIDAY, DayOff.DAYOFF_TYPE_HALF_PAID_HOLIDAY_AM,
                         DayOff.DAYOFF_TYPE_HALF_PAID_HOLIDAY_PM, DayOff.DAYOFF_TYPE_ABSENCE,
                         DayOff.DAYOFF_TYPE_HALF_ABSENCE, DayOff.DAYOFF_TYPE_LIMIT_PAID_HOLIDAY}:
            id_list = [
                DayOff.REASON_TYPE_SICK,
                DayOff.REASON_TYPE_HOUSE_WORK,
                DayOff.REASON_TYPE_OTHER
            ]
            if select_id == DayOff.DAYOFF_TYPE_LIMIT_PAID_HOLIDAY:
                remarks.append("time_able")
        elif select_id in {DayOff.DAYOFF_TYPE_SPECIAL}:
            id_list = [
                DayOff.REASON_TYPE_AUSPICIOUS,
                DayOff.REASON_TYPE_CONDOLENCE,
                DayOff.REASON_TYPE_OTHER
            ]
        else:
            id_list = []
        return HttpResponse(create_options(id_list, reason, next_id, type, remarks))
    elif type == "reason":
        if select_id in {DayOff.REASON_TYPE_AUSPICIOUS, DayOff.REASON_TYPE_CONDOLENCE}:
            id_list = [
                DayOff.DETAIL_TYPE_MARRY,
                DayOff.DETAIL_TYPE_MARRY_CHILD,
                DayOff.DETAIL_TYPE_BIRTH
            ]
            if select_id == DayOff.REASON_TYPE_CONDOLENCE:
                id_list.append(DayOff.DETAIL_TYPE_CONDOLENCE)

            remarks.append("detail_able")
        else:
            id_list = []
        return HttpResponse(create_options(id_list, detail, next_id, type, remarks))
    else:
        return redirect("vac:logout")


def create_options(ids_list, choice, next_id, type, remarks):
    _name_ = "reason_type" if type == "dayoff" else "detail_type"
    _id_ = "id_" + _name_
    disp_html = ['<select name="' + _name_ + '" class="form-control" required id="' + _id_ + '">\n']
    for elem in ids_list:
        selected = 'selected' if elem == int(next_id) else ''
        disp_html.append('<option value="' + str(elem) + '" ' + selected + '>' + choice[int(elem/10)-1][1] + '</option>\n')

    selected = 'selected' if next_id == '0' else ''
    disp_html.insert(1, "<option value " + selected + ">---------</option>\n")
    disp_html.append("</select>\n")

    for remark in remarks:
        disp_html.append("<!-- " + remark + " -->\n")
    return disp_html
