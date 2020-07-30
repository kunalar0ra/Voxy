from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('mess/',include('mess.urls')),
    path('',include('main.urls'))
]
