from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ProtectedArea, Location
from .serializers import ProtectedAreaSerializer, LocationSerializer, LocationViewSet
from django.db import connection

@csrf_exempt
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def update_something(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def protected_area_list(request):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.all()
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt  
def location_protected_areas_list(request, sub_loc):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.filter(sub_loc=sub_loc)
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def test_function(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM core_protectedarea")
            row = cursor.fetchone()
            count_value = row[0]
            #total_protected_areas = ProtectedArea.objects.raw("SELECT COUNT(*) FROM core_protectedarea")
            return HttpResponse('Total Protected Areas: ' + str(count_value))
        
@csrf_exempt
def myfancyfuction(request):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.raw("SELECT * FROM core_protectedarea")
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return JsonResponse(serializer.data, safe=False)
