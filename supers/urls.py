from django.urls import path
from . import views

urlpatterns = [
    path('', views.supersList),
    path('<int:pk>/',views.supersDetail)
]
