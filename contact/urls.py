from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.submit_form, name='contact_submit_form'),
    path('thankyou/', views.thank_you, name='thank_you'),
]
