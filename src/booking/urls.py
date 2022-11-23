
from rest_framework import routers

from django.urls import path, include

from .views import BookingViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register("booking", BookingViewset
)

urlpatterns = [
    path('', include(router.urls))
]