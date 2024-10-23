from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import UserType
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class IndexView(TemplateView):
    template_name = "website/index.html"

class ContactView(TemplateView):
    template_name = "website/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admins"] = User.objects.filter(plant=self.request.user.plant, type=UserType.admin.value)
        print(context["admins"])
        return context

class AboutView(TemplateView):
    template_name = "website/about.html"