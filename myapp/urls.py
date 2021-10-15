from rest_framework.routers import DefaultRouter

from .views import ShopingCenterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='api/v1/shopingcenters', viewset=ShopingCenterViewSet, basename="shopingcenter")

urlpatterns = router.urls