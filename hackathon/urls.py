from django.contrib import admin
from django.urls import path
import scoreapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',scoreapp.views.home, name="home"),
    path('create/', scoreapp.views.create, name="create"),
    path('nowgrade/', scoreapp.views.nowgrade, name="nowgrade"),
    path('nowgrade/happy', scoreapp.views.happy, name="happy"),
    path('nowgrade/happy/result', scoreapp.views.result, name="result"),
]