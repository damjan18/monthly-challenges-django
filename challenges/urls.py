from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:selected_month>", views.monthly_challenge_bu_number),
    path("<str:selected_month>", views.monthly_challenge, name="month-challenge")
    
    
]
