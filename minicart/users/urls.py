from django.urls import path
from .views import *

urlpatterns = [
    path("custh",CustHomeView.as_view(),name="home"),

]
