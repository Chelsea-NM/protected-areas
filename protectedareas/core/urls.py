from django.urls import path,include
from . import views
from . import api
from rest_framework import routers
urlpatterns = [
    #path('', include(routers.DefaultRouter().urls)),
    path('locations/', api.location_list, name='locationlist'),
    path('protected-areas/', api.protected_area_list, name='protectedareaslist'),
    path('location-protected-areas/<str:sub_loc>/', api.location_protected_areas_list, name='locationprotectedareaslist'),
    path('test/', api.myfancyfuction, name='testfunction')
    # Add more API endpoints here
]