from rest_framework.routers import DefaultRouter

from apps.loans.api.api import create_loans_api_view

router = DefaultRouter()

router.register('/', create_loans_api_view, basename="loans")

urlpatterns = router.urls