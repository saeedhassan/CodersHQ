from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from allauth.exceptions import ImmediateHttpResponse
from django.contrib import messages
from django.shortcuts import redirect

class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):

        
        try:
            get_user_model().objects.get(email=sociallogin.user.email)
        except get_user_model().DoesNotExist:
            messages.error(request, 'Your GitHub email is not associated with any existing user. Please Sign up firt!')
            # raise ImmediateHttpResponse(HttpResponse(status=500))
            #abort the login
            raise ImmediateHttpResponse(redirect('/accounts/login'))
        else:
            user = get_user_model().objects.get(email=sociallogin.user.email)
            if not sociallogin.is_existing:
                sociallogin.connect(request, user) 

    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)





#useful links:
#https://github.com/pennersr/django-allauth/issues/418
# https://fluffycloudsandlines.blog/using-django-allauth-for-google-login-to-any-django-app/
#https://ilovedjango.com/django/authentication/allauth/allauth-django/