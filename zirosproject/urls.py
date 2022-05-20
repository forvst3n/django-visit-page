from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from main import views as m_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',m_views.index,name='index'),
    path('about-us/',m_views.about_us,name='about_us'),
    path('contact/',m_views.contact,name='contact')
]
