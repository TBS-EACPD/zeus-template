"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views.login import LoginView
from .views.root import RootView

dev_routes = []
if settings.DEBUG and settings.ENABLE_TOOLBAR:
    import debug_toolbar

    dev_routes += [url(r"^__debug__/", include(debug_toolbar.urls))]


urlpatterns = i18n_patterns(
    url("login", LoginView.as_view(), name="login"),
    url("logout", LogoutView.as_view(), name="logout"),
    url("firstapp/", include(("firstapp.urls", "firstapp"), namespace="firstapp")),
) + [
    path("admin/", admin.site.urls),
    url(r"^session_security/", include("session_security.urls")),
    *dev_routes,
    url(r"/", RootView.as_view(), name="root"),
]
