from django.urls import path, include
from .views import *

urlpatterns = [path("checkBanned/", CheckBanned.as_view())]
