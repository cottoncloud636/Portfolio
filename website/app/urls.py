# from django.contrib import admin
from app import views #from the app folder, import the views.py file
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


"""
don't forget to add "," -- comma, after each path
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include ('app.urls') )
    path('', views.home, name="home"), #whenever I redirect to the home page, I want to run the "index" function from the views 
    #name is an optional attribute, here means the funtion name should be exactly "index", it shouldn't
    #be any other name.
    path('about', views.about, name="about"), #whever there is a "/about", I should run the about function in view
    path('resume', views.resume, name='resume'),
    path('projects', views.projects, name='projects'),
    path('projects/project/<str:pk>/', views.project, name='project'),

    path('projects/like/<int:project_id>/', views.like_project, name='like_project'),

    path('contact', views.contact, name="contact"),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)