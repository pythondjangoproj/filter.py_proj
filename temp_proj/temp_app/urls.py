# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'temp_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.sample_view, name='sample_view'),
]
