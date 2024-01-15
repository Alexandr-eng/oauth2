from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, names='index'),
    path('account/profile/', views.profile, names='profile'),
    path('social/', include('social_django.urls', namespace='social_auth')),

]