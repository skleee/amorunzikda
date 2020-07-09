from django.contrib import admin
from django.urls import path
import scoreapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scoreapp.views.home, name="home"),
    path('create/', scoreapp.views.create, name="create"),
    path('happycircuit/', scoreapp.views.happycircuit, name="happycircuit"),
    # path('conclusion/', scoreapp.views.conclusion, name="conclusion"),
    # path('nowgrade/', scoreapp.views.nowgrade, name="nowgrade"),
    path('happy/', scoreapp.views.happy, name="happy"),
    path('happy/result/', scoreapp.views.result, name="result"),
    path('happy/result/create', scoreapp.views.result_submit, name="result_submit"),
    path('about/', scoreapp.views.about, name="about"),
]
