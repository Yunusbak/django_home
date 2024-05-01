from django.urls import path
from users.views import get_info

urlpatterns = [
    path("app1/", get_info, name="get_info")
]