from django.urls import path,include
from .. import views


urlpatterns = [
    path("user/list/", views.UserListView.as_view(), name="user-list"),
    path("user/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("user/<int:pk>/edit/", views.UserUpdateView.as_view(), name="user-edit"),
    path("user/create/", views.UserCreateView.as_view(), name="user-create"),

    path("user/security/edit/<int:pk>",views.AdminSecurityEditUserView.as_view(),name="admin-security-edit"),
    path("user/profile/edit/<int:pk>",views.AdminProfileEditUserView.as_view(),name="admin-profile-edit"),
    path("user/profile/image/edit/<int:pk>",views.AdminProfileImageEditUserView.as_view(),name="profile-image-edit"),
]