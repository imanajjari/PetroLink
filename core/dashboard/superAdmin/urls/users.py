from django.urls import path,include
from .. import views


urlpatterns = [
    #customers
    path("user/list/", views.UserListView.as_view(), name="user-list"),
    path("user/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("user/<int:pk>/edit/", views.UserUpdateView.as_view(), name="user-edit"),
    #admins
    path("admin/list/", views.AdminListView.as_view(), name="admin-list"),
    path("admin/<int:pk>/delete/", views.AdminDeleteView.as_view(), name="admin-delete"),
    path("admin/create", views.AdminCreateView.as_view(), name="admin-create"),
    path("admin/<int:pk>/edit/", views.AdminUpdateView.as_view(), name="admin-edit"),

    path("admin/security/edit/<int:pk>",views.AdminSecurityEditUserView.as_view(),name="admin-security-edit"),
    path("admin/profile/edit/<int:pk>",views.AdminProfileEditView.as_view(),name="profile-edit"),
    path("admin/profile/image/edit/<int:pk>",views.AdminProfileImageEditView.as_view(),name="profile-image-edit"),

    # create user
    path("user/create/",views.SuperAdminUserCreateView.as_view(),name="superadmin-create-user"),


]