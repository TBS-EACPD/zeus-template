from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseNotFound, HttpResponseServerError
from django.urls import reverse
from django.views.generic import RedirectView

from firstapp import constants


class RootView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse("login")
        user = self.request.user
        if constants.BUSINESS_ADMIN_GROUP_NAME in user.group_names:
            return reverse("first-app:admin-home")
        if constants.DEPT_GROUP_NAME in user.group_names:
            dept_id = user.dept_profile.department_id
            return reverse("first-app:dept-home", args=[dept_id])

        raise Exception("expected user type")
