from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("management/dashboard/", views.dashboard, name='dashboard'),
    path("management/res/apartment/request", views.management_res_apartment_request,
         name='management_res_apartment_request'),
    path("management/all/apartment/request", views.management_all_apartment_request,
         name='management_all_apartment_request'),
    path("management/daily/apartment/request", views.management_daily_apartment_request,
         name='management_daily_apartment_request'),

    path("management/weekly/apartment/request", views.management_weekly_apartment_request,
         name='management_weekly_apartment_request'),

    path("management/res/apartment/request/detail/<int:id>/<int:pk>", views.management_res_apartment_request_detail,
         name='management_res_apartment_request_detail'),

    path("management/comm/apartment/request/detail/<int:id>/<int:pk>", views.management_comm_apartment_request_detail,
         name='management_comm_apartment_request_detail'),

    path("management/apartment/pending", views.management_apartment_pending,
         name='management_apartment_pending'),

    path("management/apartment/no/vacancy", views.apartment_no_vacancy,
         name='apartment_no_vacancy'),

    path("management/apartment/detail/<int:pk>", views.management_res_apartment_detail,
         name='management_res_apartment_detail'),

    path("management/apartment/detail/comm/<int:pk>", views.management_comm_apartment_detail,
         name='management_comm_apartment_detail'),

    path("management/apartment/all", views.management_apartment_all,
         name='management_apartment_all'),

    path("management/apartment/unapproved", views.management_apartment_unapproved,
         name='management_apartment_unapproved'),

    path("management/agent/list", views.agent_list,
         name='agent_list'),

    path("management/search/apartment", views.search_apartment,
         name='search_apartment'),


    path("management/agent/details/<int:pk>", views.agent_details,
         name='agent_details'),

    path("management/landlord/list", views.landlord_list,
         name='landlord_list'),

    path("management/landlord/details/<int:pk>", views.landlord_details,
         name='landlord_details'),

    path("management/Service/fee", views.service_fee, name='service_fee'),

    path("management/agent/fee", views.agent_fee, name='agent_fee'),

    path("management/revenue/manager", views.revenue_manager, name='revenue_manager'),

    path("management/payment", views.payment, name='payment'),

    path("management/staff_/login", views.staff_login, name='staff_login'),

    path("management/agent_payment_request/", views.agent_payment_request, name='agent_payment_request'),

    path("management/agent_payment_request/details/<int:pk>", views.request_detail, name='request_detail'),

    path("management/request/paid/<int:pk>/", views.paid, name='paid'),

    path("management/request/failed/<int:pk>/", views.failed, name='failed'),

    path("management/payment/failed/", views.failed_payment, name='failed_payment'),

    path("management/payment/paid/", views.paid_agent, name='paid_agent'),

    path("management/expenses_list/", views.expenses_list, name='expenses_list'),

    path("management/add_expenses/", views.add_expenses, name='add_expenses'),

    path("management/all_expenses/", views.expenses_all, name='expenses_all'),

    path("feedback/form/", views.feedback_form, name='feedback_form'),

    path("feedback/", views.feedback, name='feedback'),

    path("feedback/sent", views.feedback_sent, name='feedback_sent'),

    path("feedback/list", views.feedback_list, name='feedback_list'),

    path("management/rate/res/<int:pk>/", views.rate_res, name='rate_res'),

    path("management/rate/com/<int:pk>/", views.rate_com, name='rate_com'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
