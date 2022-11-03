"""Agent41 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Clients_profile.urls")),
    path("", include("User_Profiles.urls")),
    path("", include("Apartments.urls")),
    path("", include("Management.urls")),
    path("", include("Agents.urls")),

]

admin.site.site_header = "Agent41 Management Database"
admin.site.site_title = "Agent41 Admin Portal"
admin.site.index_title = "Welcome to Agent41 Management Portal"
