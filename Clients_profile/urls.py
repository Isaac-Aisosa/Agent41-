from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #path("management/dashboard/", views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
