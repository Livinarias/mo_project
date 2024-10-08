"""
URL configuration for mo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.customers.views import upload_file, home_page
"""This is the urls that consume endpoints order by modules"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='Upload File'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer/create_with_csv/', upload_file, name='create_customer'),
    path('customer/',include('apps.customers.api.urls')),
    path('loan/',include('apps.loans.api.urls')),
    path('payment/',include('apps.payments.api.urls')),
]
