from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import get_user_model
User = get_user_model()



class AdminDashboardHomeView(LoginRequiredMixin, HasAdminAccessPermission, TemplateView):
    template_name = "dashboard/admin/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(id=self.request.user.id)
        return context
