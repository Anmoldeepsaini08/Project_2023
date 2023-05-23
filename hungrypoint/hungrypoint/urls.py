
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='home'),
    path('menu',views.menu,name='menu'),
    path('booktable',views.table_book,name='booktable'),
    path('contactform',views.contact_form,name='contactform'),
    
    path('admin/',include('admin_pannel.urls'))


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
