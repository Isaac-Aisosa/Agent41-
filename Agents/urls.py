from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("agent_index/", views.agent_index, name='agent_index'),
    #path("agent/apartment/details/<int:pk>/", views.agent_apartment_details, name='agent_apartment_details'),
    #path("agent/commercial/apartment/details/<int:pk>/", views.agent_commercial_apartment_details,
    #     name='agent_commercial_apartment_details'),
    path("agent_signup/", views.agent_signup, name='agent_signup'),
    path("agent_profile/", views.create_agent_profile, name='agent_profile'),
    path("agent_login/", views.agent_login, name='agent_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("agent/select/form", views.agent_select_form, name='agent_select_form'),
    path("agent/residential/apartment/form", views.agent_residential_apartment_form,
         name='agent_residential_apartment_form'),
    path("agent/commercial/apartment/form", views.agent_commercial_apartment_form,
         name='agent_commercial_apartment_form'),
    path("agent_profile2/", views.agent_profile, name='agent_profile2'),
    path("payment/form/edit/", views.edit_payment, name='edit_payment'),
    path("payment/form/", views.paymentform, name='paymentform'),
    path("agent/requestpay/", views.requestpay, name='requestpay'),
    path("agent/edit/", views.edit_agent_profile, name='edit_agent_profile'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
