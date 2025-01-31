from django.urls import path
from . import views

urlpatterns = [
    path('generate-password',views.random_password),
    path('generate-number',views.random_number)
]
