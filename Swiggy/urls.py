from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('res/',include("restaurant.urls")),
    path('admin/',include("s_admin.urls")),
    path('superadmin/', admin.site.urls),
]
