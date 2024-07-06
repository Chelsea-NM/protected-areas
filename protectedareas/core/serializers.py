from rest_framework import routers, serializers, viewsets
from .models import ProtectedArea,Location

# Serializers define the API representation.
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProtectedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectedArea
        fields = '__all__'

# ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# ViewSets define the view behavior.
class ProtectedAreaViewSet(viewsets.ModelViewSet):
    queryset = ProtectedArea.objects.all()
    serializer_class = ProtectedAreaSerializer

    

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'protectedareas', ProtectedAreaViewSet)
