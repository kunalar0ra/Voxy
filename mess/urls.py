from django.urls import path
from mess import views
urlpatterns = [
    path('<int:pk>/',views.privatemessage.as_view())
]