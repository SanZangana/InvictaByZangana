from . import views
from django.urls import path

# Difference between this urls.py and the other urls.py in 'saninvicta' foldeR?
urlpatterns = [
    path('', views.home, name='home'),
    path('membership/', views.ReviewList.as_view(), name='membership'),
    path('membership/<slug:slug>/', views.ReviewDetail.as_view(), name='review'),
    path('add_review/', views.add_review, name='add_review'),
    path('update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]