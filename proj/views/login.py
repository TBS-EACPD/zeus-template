from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views import View


class LoginView(BaseLoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("root-home"))
        else:
            return super().get(request, *args, **kwargs)
