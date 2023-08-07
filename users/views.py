from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLoginView


class LoginView(BaseLoginView):
    pass


class LogoutView(BaseLoginView):
    pass
