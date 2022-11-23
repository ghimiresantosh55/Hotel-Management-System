from rest_framework import routers

from django.urls import path, include

from .views import CustomerViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register("customer", CustomerViewset
)

urlpatterns = [
    path('', include(router.urls))
]