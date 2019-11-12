from django.contrib import admin 
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', include('users.urls')),
    path('', include('dashboard.urls')),
    path('kpis', include('KPIs.urls')),
]
