from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static
from .views import Residential, Commercial
urlpatterns = [

    path("", views.index, name='index'),
    path("select/form", views.select_form, name='select_form'),
    path("select/type", views.select_type, name='select_type'),
    path("residential/detail/<int:pk>", views.residential_details, name='residential_details'),
    path("commercial/detail/<int:pk>", views.commercial_details, name='commercial_details'),
    path('search/residential/apartment/', views.search_residential, name='search_residential'),
    path('search/commercial/apartment/', views.search_commercial, name='search_commercial'),
    path('filter/commercial/apartment/', views.filter_commercial, name='filter_commercial'),
    path('filter/residential/apartment/', views.filter_residential, name='filter_residential'),
    path('residential', Residential.as_view(),  name="residential"),
    path('commercial', Commercial.as_view(),  name="commercial"),
    path("residential/apartment/form", views.residential_apartment_form, name='residential_apartment_form'),
    path("commercial/apartment/form", views.commercial_apartment_form, name='commercial_apartment_form'),
    path("residential/apartment/request<int:pk>", views.residential_apartment_request, name='residential_request'),
    path("residential/get/apartment/", views.get_residential_apartment, name='get_residential_apartment'),
    path("commercial/apartment/request<int:pk>", views.commercial_apartment_request, name='commercial_request'),
    path("commercial/get/apartment/", views.get_commercial_apartment, name='get_commercial_apartment'),
    path("apartment/confirm/request<int:pk>", views.confirm_apartment, name='confirm_apartment'),
    path("apartment/confirm/request/comm/<int:pk>", views.confirm_apartment_comm, name='confirm_apartment_comm'),
    path("apartment/approve/apartment/<int:pk>", views.approve_res_apartment, name='approve_res_apartment'),
    path("apartment/approve/apartment/comm/<int:pk>", views.approve_comm_apartment, name='approve_comm_apartment'),
    path("apartment/unapprove/apartment/<int:pk>", views.unapprove_res_apartment, name='unapprove_res_apartment'),
    path("apartment/unapprove/apartment/comm/<int:pk>", views.unapprove_comm_apartment, name='unapprove_comm_apartment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
