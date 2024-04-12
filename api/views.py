from rest_framework import viewsets
from entity.models import SubMoney,AddMoney
from .serializers import SubMoneySerializer,AddMoneySerializer
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.db.models import Q
from datetime import datetime


class AddMoneyDateRangeView(APIView):
     def get(self, request):
        start_date_str = self.request.query_params.get('start_date')
        end_date_str = self.request.query_params.get('end_date')
        
        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({'error': 'Invalid date format'}, status=400)

            addmoney_queryset = AddMoney.objects.filter(
                Q(created_at__gte=start_date) & Q(created_at__lte=end_date)
            )
        else:
            addmoney_queryset = AddMoney.objects.all()

        addMoneySerializer = AddMoneySerializer(addmoney_queryset, many=True)
        return Response(addMoneySerializer.data, status=200)

class SubMoneyDateRangeView(APIView):
    def get(self,request):
        start_date_str = self.request.query_params.get('start_date')
        end_date_str = self.request.query_params.get('end_date')
        
        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({'error': 'Invalid date format'}, status=400)

            submoney_queryset = SubMoney.objects.filter(
                Q(created_at__gte=start_date) & Q(created_at__lte=end_date)
            )
            
        else:
            submoney_queryset = SubMoney.objects.all()

        subMoneySerializer = SubMoneySerializer(submoney_queryset, many=True)
        return Response(subMoneySerializer.data, status=200)
class SubMoneyViewSet(viewsets.ModelViewSet):
    queryset = SubMoney.objects.all()
    serializer_class = SubMoneySerializer
class AddMoneyViewSet(viewsets.ModelViewSet):
    queryset = AddMoney.objects.all()
    serializer_class = AddMoneySerializer