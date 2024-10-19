from django.urls import path,include
from .. import views

urlpatterns = [


    path("security/edit/",views.SuperAdminSecurityEditView.as_view(),name="super-admin-security-edit"),
    path("profile/edit/",views.SuperAdminProfileEditView.as_view(),name="super-admin-profile-edit"),
    path("profile/image/edit/",views.SuperAdminProfileImageEditView.as_view(),name="super-admin-profile-image-edit"),
]

