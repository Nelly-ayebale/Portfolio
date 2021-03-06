from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   path('',views.home,name="home"),
   path('about/',views.about,name="about"),
   path('skills/',views.skills,name="skills"),
   path('projects/',views.projects,name="projects"),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
