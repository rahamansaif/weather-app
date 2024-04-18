from rest_framework.response import Response
from rest_framework.decorators import api_view

from weather.models import Weather
from weather.serializers import WeatherSerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = WeatherSerializer(data=request.data)
        serializer.save()
        return Response(data=serializer.data, status='201')
