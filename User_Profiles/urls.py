from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("landlord_index/", views.landlord_index, name='landlord_index'),
    path("landlord/apartment/details/<int:pk>/", views.landlord_apartment_details, name='landlord_apartment_details'),
    path("landlord/commercial/apartment/details/<int:pk>/", views.landlord_commercial_apartment_details,
         name='landlord_commercial_apartment_details'),
    path("landlord_signup/", views.landlord_signup, name='landlord_signup'),
    path("landlord_profile/", views.create_landlord_profile, name='landlord_profile'),
    path("landlord/profile", views.landlord_profile, name='landlord_profile2'),
    path("landlord_login/", views.landlord_login, name='landlord_login'),
    path("landlord/edit", views.edit_landlord_profile, name='edit_landlord_profile'),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
