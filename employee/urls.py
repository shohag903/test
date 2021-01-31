
from employee import views
from django.urls import path

urlpatterns = [
    path('', views.employee),
    path('profile/', views.profile, name='employee.profile'),
]