from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubMoneyViewSet,AddMoneyViewSet
from .views import SubMoneyDateRangeView,AddMoneyDateRangeView
router = DefaultRouter()
router.register(r'submoney', SubMoneyViewSet)
router.register(r'addmoney', AddMoneyViewSet)
urlpatterns = [
    path('', include(router.urls)),
  
    path('submoneys/date_range/', SubMoneyDateRangeView.as_view(), name='submoney-date-range'),
    path('addmoneys/date_range/', AddMoneyDateRangeView.as_view(), name='addmoney-date-range'),

]
