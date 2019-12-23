from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    # return HttpResponse('休暇管理システムメニュー')
    return render(request, 'vac/index.html')
