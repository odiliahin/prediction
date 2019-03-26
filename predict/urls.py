from django.urls import path

from . import views


urlpatterns = [
    path('prediction_for_day_result/', views.predictions_for_day_list, name='predictions_for_day_list'),
    path('', views.index, name='index'),
]
