from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.models import UserType


class DashboardHomeView(LoginRequiredMixin,View):
    
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            # simple example of print for fix code
            # print(f'\n\n\n\n{request.user.type}')
            # print(f'\n\n\n\n{UserType.customer.value}')
            if request.user.type == UserType.customer.value:
                return redirect(reverse_lazy('dashboard:customer:home'))
            if request.user.type == UserType.admin.value:
                return redirect(reverse_lazy('dashboard:admin:home'))
        else:
            return redirect(reverse_lazy('accounts:login'))
        return super().dispatch(request, *args, **kwargs)
    
    