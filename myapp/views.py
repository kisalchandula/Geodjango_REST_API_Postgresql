from rest_framework import viewsets, status
from .models import ShopingCenter
from .serializers import ShopingCenterSerialzer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django_filters.rest_framework import DjangoFilterBackend

class ShopingCenterViewSet(viewsets.ModelViewSet):
    queryset = ShopingCenter.objects.all()
    serializer_class = ShopingCenterSerialzer
    filter_backends=(DjangoFilterBackend,)


    @action(detail=False, methods=["get"])
    def closest_shopingcenters(self, request):
        """Get centers that are at least 3 km from user location"""
        longitude=request.GET.get("lon",None)
        latitude=request.GET.get("lat",None)

        if longitude and latitude:
            user_location=Point(float(longitude), float(latitude), srid=4326)
            closest_shopingcenters = ShopingCenter.objects.filter(location__distance_lte=
            (user_location,D(km=3)))
            serializer=self.get_serializer_class()
            serialized_shopingcenters=serializer(closest_shopingcenters, many=True)
            return Response(serialized_shopingcenters.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def new_method(self, user_location):
        closest_shopingcenters=ShopingCenter.objects.all.filter(geom__distance_lte=(user_location,D(km=3)))
        return closest_shopingcenters
