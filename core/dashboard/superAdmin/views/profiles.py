from django.views.generic import View, TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasSuperAdminAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from django.shortcuts import redirect
from django.contrib import messages


class SuperAdminSecurityEditView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/superAdmin/profile/security-edit.html"
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:superAdmin:super-admin-security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"


class SuperAdminProfileEditView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/superAdmin/profile/profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:superAdmin:super-admin-profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

class SuperAdminProfileImageEditView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:superAdmin:super-admin-profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)