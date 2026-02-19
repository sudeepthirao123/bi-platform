
from django.urls import path
from analytics.views import sales_summary

urlpatterns = [
    path('api/sales/', sales_summary),
]
