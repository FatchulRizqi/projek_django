from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
from contact import views as contactViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('about/', include("about.urls")),
    path('contact/', contactViews.contact, name='contact'),
]
