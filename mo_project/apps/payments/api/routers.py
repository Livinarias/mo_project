from rest_framework.routers import DefaultRouter

from apps.payments.api.api import create_payments_api_view

router = DefaultRouter()

router.register('/', create_payments_api_view, basename="payments")

urlpatterns = router.urls