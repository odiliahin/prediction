from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('prediction_for_day_result/', views.predictions_for_day_list, name='predictions_for_day_list'),
    path('choose_prediction/', views.choose_prediction, name='choose_prediction'),
]
