from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import TransactionViewSet

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet)

urlpatterns = router.urls
