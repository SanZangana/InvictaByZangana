from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('membership/', views.ReviewList.as_view(), name='membership'),
    path('membership/<slug:slug>/', views.ReviewDetail.as_view(), name='review'),
]