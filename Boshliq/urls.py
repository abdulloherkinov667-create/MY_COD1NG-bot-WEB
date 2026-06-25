
from django.contrib import admin
from django.urls import path
from app.views import home_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_menu, name='home_menu'),

]
