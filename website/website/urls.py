from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('about/', include("about.urls")),
    path('contact/', include("contact.urls")),
]
