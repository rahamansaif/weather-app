from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from weather.models import Weather
from weather.serializers import WeatherSerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status='201')
        else:
            return Response(data=request.data, status=422)
    if request.method == 'GET':
        date = request.GET.get('date')
        city = request.GET.get('city')
        sort = request.GET.get('sort')
        weather_data = Weather.objects.all()
        if date:
            weather_data = weather_data.filter(date=date)
        if city:
            weather_data = weather_data.filter(city__iexact=city)
        if sort:
            weather_data = weather_data.order_by(sort, 'id')
        serializer = WeatherSerializer(weather_data, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def weather_details(request, id):
    try:
        weather_object = Weather.objects.get(id=id)
        serializer = WeatherSerializer(weather_object)
        return Response(data=serializer.data)
    except(Weather.DoesNotExist):
        raise Http404
