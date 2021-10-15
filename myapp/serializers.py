from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import  ShopingCenter

class ShopingCenterSerialzer(GeoFeatureModelSerializer):
    class Meta:
        model=ShopingCenter
        geo_field="location"
        fields= "__all__"
