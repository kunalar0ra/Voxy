from django.conf import settings
from django.urls import path
from main import views
from django.conf.urls.static import static
urlpatterns = [
  path('home/', views.Home.as_view()),
  path('post/', views.Post.as_view()),
  path('post/<int:pk>/like/', views.PostLike.as_view()),
  path('request/<int:pk>/add/', views.Sendrequest.as_view()),
  path('add/<int:pk>/friend/', views.addfriend.as_view()),
  path('cancel/<int:pk>/friend/', views.cancelrequest.as_view()),
  path('post/<int:pk>/comment/', views.PostComment.as_view()),
 # path('editprofile/<int:user.pk>/',views.Edit.as_view()),
  path('id/<int:pk>/',views.Seeid.as_view() , name='seeid'),
  path('friends/',views.Friends.as_view()),
  path('wall/', views.Wall.as_view()),
  path('', views.Wall.as_view())
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)