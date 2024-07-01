# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/weekly_summary/', views.get_weekly_summary, name='weekly_summary'),
    path('api/monthly_summary/', views.get_monthly_summary, name='monthly_summary'),
    path('api/yearly_summary/', views.get_yearly_summary, name='yearly_summary'),
    path('api/weekly_summary_price/', views.get_weekly_summary_price, name='weekly_summary_price'),
    path('api/monthly_summary_price/', views.get_monthly_summary_price, name='monthly_summary_price'),
    path('api/yearly_summary_price/', views.get_yearly_summary_price, name='yearly_summary_price'),
]
