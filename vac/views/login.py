from django.shortcuts import render, redirect


from vac.forms import LoginForm


def login_view(request):
    """ログイン"""

    """
    ログイン状態でメニューへリダイレクトされません
    if request.user.is_authenticated():
        return redirect('vac:vacation_menu')
    """

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            if form.login(request):
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect('vac:vacation_menu')
    else:
        form = LoginForm()

    return render(request, 'vac/login.html', dict(form=form))
