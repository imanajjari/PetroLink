from django.urls import path,include

app_name = "superAdmin"

urlpatterns = [
    path("",include("dashboard.superAdmin.urls.generals")),
    path("",include("dashboard.superAdmin.urls.profiles")),
    path("",include("dashboard.superAdmin.urls.products")),
    path("",include("dashboard.superAdmin.urls.orders")),
    path("",include("dashboard.superAdmin.urls.reviews")),
    path("",include("dashboard.superAdmin.urls.newsletters")),
    path("",include("dashboard.superAdmin.urls.contacts")),
    path("",include("dashboard.superAdmin.urls.users")),
    path("",include("dashboard.superAdmin.urls.coupons")),
]


