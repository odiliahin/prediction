from django.shortcuts import render
from .models import PredictionsForDay


def predictions_for_day_list(request):
    prediction = PredictionsForDay.objects.order_by('?')[:1]
    return render(request, 'predict/predictions_for_day_list.html', {'prediction': prediction})


def index(request):
    return render(request, 'predict/index.html')
