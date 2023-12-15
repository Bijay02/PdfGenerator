from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
    path('user', views.user, name="user"),
    path('pdf',GeneratePdf.as_view(), name='pdf')
]