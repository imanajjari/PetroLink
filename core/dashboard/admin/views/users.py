from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import *
from django.db.models import F,Q
from django.core import exceptions
from django.contrib.auth import get_user_model
from dashboard.admin.forms import *
User = get_user_model()





class UserListView(LoginRequiredMixin,HasAdminAccessPermission, ListView):
    title = "لیست کاربران"
    template_name = "dashboard/admin/users/user-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=False,type=UserType.customer.value, plant=self.request.user.plant)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass

        search_query = self.request.GET.get('q', None)
        ordering_query = self.request.GET.get('ordering', None)

        if search_query:
            queryset = queryset.filter(
                 Q(email__icontains=search_query)|Q(id__icontains=search_query)
            )
        if ordering_query:
            try:
                queryset = queryset.order_by(ordering_query)
            except exceptions.FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_result"] = self.get_queryset().count()
        return context



class UserDeleteView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin, DeleteView):
    title = "حذف کاربر"
    template_name = "dashboard/admin/users/user-delete.html"
    success_url = reverse_lazy("dashboard:admin:user-list")
    success_message = "کاربر مورد نظر با موفقیت حذف شد"
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.customer.value)
    
    
class UserUpdateView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin, UpdateView):
    title = "ویرایش کاربر"
    template_name = "dashboard/admin/users/user-edit.html"
    success_message = "کاربر مورد نظر با موفقیت ویرایش شد"
    form_class = UserForm
    
    
    def get_success_url(self) -> str:
        return reverse_lazy("dashboard:admin:user-edit",kwargs={"pk":self.kwargs.get("pk")})
    
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.customer.value)


class UserCreateView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/users/user-create.html"
    form_class = AdminUserCreationForm
    success_url = reverse_lazy("dashboard:admin:user-create")
    success_message = 'کاربر با موفقیت ایجاد شد.'

    def form_valid(self, form):
        super().form_valid(form)
        admin = Profile.objects.get(user=self.request.user)
        user = form.save(commit=False)
        user.admin = admin.user
        user.plant = admin.plant
        user.save()
        user = User.objects.get(email=form.cleaned_data['email'])
        return redirect("dashboard:admin:admin-profile-edit", pk=user.id)

# profile admins

class AdminSecurityEditUserView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/users/admin-security-edit.html"
    form_class = AdminChangePasswordUserForm
    model = User
    success_url = reverse_lazy("dashboard:admin:user-list")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request,'رمز عبور کاربر با موفقیت تغییر یافت.')
        super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)

class AdminProfileEditUserView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/users/admin-profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:admin:user-list")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.kwargs.get("pk"))

class AdminProfileImageEditUserView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:admin:user-list")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.kwargs.get("pk"))
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)