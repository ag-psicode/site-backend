from django.urls import include, path
from rest_framework import routers
from estimates.views import EstimateRequestViewSet

router = routers.SimpleRouter()
router.register(r'estimates', EstimateRequestViewSet, base_name="estimates")

urlpatterns = [
    path('', include(router.urls)),
]