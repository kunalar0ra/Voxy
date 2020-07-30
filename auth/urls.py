from django.urls import path
from auth import views
urlpatterns = [
    path('login/',views.loginreq.as_view()),
    path('logout/',views.logout.as_view()),
   path('signup/',views.signupreq.as_view())
]