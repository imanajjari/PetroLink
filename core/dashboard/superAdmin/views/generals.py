from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasSuperAdminAccessPermission


class AdminDashboardHomeView(LoginRequiredMixin, HasSuperAdminAccessPermission, TemplateView):
    template_name = "dashboard/superAdmin/home.html"
