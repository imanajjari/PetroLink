from django.urls import path, include
from .. import views


urlpatterns = [
    path("product/list/",views.SuperAdminProductListView.as_view(),name="product-list"),
    path("product/create/",views.SuperAdminProductCreateView.as_view(),name="product-create"),
    path("product/<int:pk>/edit/",views.SuperAdminProductEditView.as_view(),name="product-edit"),
    path("product/<int:pk>/delete/",views.SuperAdminProductDeleteView.as_view(),name="product-delete"),
    path("product/<int:pk>/add-image/",views.SuperAdminProductAddImageView.as_view(),name="product-add-image"),
    path("product/<int:pk>/image/<int:image_id>/remove/",views.SuperAdminProductRemoveImageView.as_view(),name="product-remove-image"),
    path("product/<int:pk>/add-file/",views.SuperAdminProductAddFileView.as_view(),name="product-add-file"),
    path("product/<int:pk>/file/<int:file_id>/remove/",views.SuperAdminProductRemoveFileView.as_view(),name="product-remove-file"),
]
