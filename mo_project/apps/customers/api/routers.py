from rest_framework.routers import DefaultRouter

from apps.customers.api.api import customers_api_view

router = DefaultRouter()

router.register('/', customers_api_view, basename="customers")

urlpatterns = router.urls