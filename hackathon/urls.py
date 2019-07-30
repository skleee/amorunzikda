from django.contrib import admin
from django.urls import path
import scoreapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',scoreapp.views.home, name="home"),
    path('create/', scoreapp.views.create, name="create"),
]
