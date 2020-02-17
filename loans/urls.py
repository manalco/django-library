from rest_framework import routers
from .viewsets import LoanViewSet


router = routers.SimpleRouter()
router.register('loans', LoanViewSet)


urlpatterns = router.urls