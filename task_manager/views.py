from django.shortcuts import render
from task_manager.users.forms import LoginForm
from django.utils.translation import gettext as _
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


class Login(LoginView):

    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Welcome, {user}')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect data entered')
        return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('main_page')