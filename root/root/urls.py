from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', 'api.urls'),
    path('user/', include('userprofiles.urls')),
    path('main/', include('main.urls')),
]
