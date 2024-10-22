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
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import *
from django.db.models import F,Q
from django.core import exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import *
User = get_user_model()
from django.contrib import messages




class UserListView(LoginRequiredMixin,HasSuperAdminAccessPermission, ListView):
    title = "لیست کاربران"
    template_name = "dashboard/superAdmin/users/user-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)
    

    def get_queryset(self):
        queryset = User.objects.filter(type=UserType.customer.value).order_by("-created_date")
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



class UserDeleteView(LoginRequiredMixin,HasSuperAdminAccessPermission,SuccessMessageMixin, DeleteView):
    title = "حذف کاربر"
    template_name = "dashboard/superAdmin/users/user-delete.html"
    success_url = reverse_lazy("dashboard:superAdmin:user-list")
    success_message = "کاربر مورد نظر با موفقیت حذف شد"
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.customer.value)
    
    
class UserUpdateView(LoginRequiredMixin,HasSuperAdminAccessPermission,SuccessMessageMixin, UpdateView):
    title = "ویرایش کاربر"
    template_name = "dashboard/superAdmin/users/user-edit.html"
    success_message = "کاربر مورد نظر با موفقیت ویرایش شد"
    form_class = UserForm
    
    
    def get_success_url(self) -> str:
        return reverse_lazy("dashboard:superAdmin:user-edit",kwargs={"pk":self.kwargs.get("pk")})
    
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.customer.value)




class AdminListView(LoginRequiredMixin,HasSuperAdminAccessPermission, ListView):
    title = "لیست کاربران"
    template_name = "dashboard/superAdmin/users/admin-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)
    

    def get_queryset(self):
        queryset = User.objects.filter(type=UserType.admin.value).order_by("-created_date")
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



class AdminDeleteView(LoginRequiredMixin,HasSuperAdminAccessPermission,SuccessMessageMixin, DeleteView):
    title = "حذف کاربر"
    template_name = "dashboard/superAdmin/users/admin-delete.html"
    success_url = reverse_lazy("dashboard:superAdmin:user-list")
    success_message = "کاربر مورد نظر با موفقیت حذف شد"
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.customer.value)
    
    
class AdminUpdateView(LoginRequiredMixin,HasSuperAdminAccessPermission,SuccessMessageMixin, UpdateView):
    title = "ویرایش کاربر"
    template_name = "dashboard/superAdmin/users/admin-edit.html"
    success_message = "کاربر مورد نظر با موفقیت ویرایش شد"
    form_class = UserForm
    
    
    def get_queryset(self):
        return User.objects.filter(is_superuser=False,type=UserType.admin.value)
    
    def get_success_url(self) -> str:
        return reverse_lazy("dashboard:superAdmin:admin-edit",kwargs={"pk":self.kwargs.get("pk")})

class AdminCreateView(LoginRequiredMixin, HasSuperAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/superAdmin/users/admin-create.html"
    queryset = ProductModel.objects.all()
    form_class = UserForm
    success_message = "ایجاد محصول با موفقیت انجام شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:superAdmin:product-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:superAdmin:product-list")


# profile admins

class AdminSecurityEditUserView(LoginRequiredMixin, HasSuperAdminAccessPermission, SuccessMessageMixin, UpdateView):
    print("constarctor")
    template_name = "dashboard/superAdmin/users/admin-security-edit.html"
    form_class = AdminChangePasswordUserForm
    model = User
    success_url = reverse_lazy("dashboard:superAdmin:admin-list")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"

    def get_object(self, queryset=None):
        print("set obj")
        return User.objects.get(pk=self.kwargs.get("pk"))

    # # def test_func(self):
    # #     return self.request.user.is_superuser

    def form_valid(self, form):
        print("form_valid")
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request,'رمز عبور کاربر با موفقیت تغییر یافت.')
        super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        print("form_invalid")
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)


class AdminProfileEditView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/superAdmin/users/admin-profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:superAdmin:admin-list")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.kwargs.get("pk"))


        

class AdminProfileImageEditView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:superAdmin:admin-list")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.kwargs.get("pk"))
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)


class SuperAdminUserCreateView(LoginRequiredMixin, HasSuperAdminAccessPermission,SuccessMessageMixin,CreateView):
    template_name = "dashboard/superAdmin/users/create-user.html"
    form_class = SuperUserCreationForm
    success_url = reverse_lazy("dashboard:superAdmin:home")
    success_message = 'کاربر با موفقیت ایجاد شد.'
    
    # def form_valid(self, form):
    #     user = form.save()
    #     messages.success(self.request, 'کاربر با موفقیت ایجاد شد.')
    #     return super().form_valid(form)

