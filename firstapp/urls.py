from django.urls import path

from .views.admin_home import AdminHome
from .views.dept_home import DeptHome
from .views.update_report import UpdateReport

urlpatterns = [
    path(r"admin-home/", AdminHome.as_view(), name="admin-home"),
    path(r"home/<int:dept_id>/", DeptHome.as_view(), name="dept-home"),
    path(r"reports/<int:pk>/update", UpdateReport.as_view(), name="update-report"),
]
