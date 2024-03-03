from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('admin/users/', views.home, name="users"),
    path('admin/users/statistics/', views.statistics, name="statistics"),
    path('admin/configuration/', views.configuration, name="configuration"),
]
