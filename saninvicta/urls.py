from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('project.urls'), name='project_urls'),
    path('todo/', include('todo.urls'), name='todo_urls'),
    path('accounts/', include('allauth.urls')),
    # Add correct name to 'name', maybe 'Leave a review' or smth
]
