from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin', views.index,name='admin'),
    path('manage',views.manage,name='manage'),
    path('tables',views.tables,name='tables'),
    path('contact',views.contact,name='contact'),
    path('subscriber',views.subscribe,name='subscriber'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
