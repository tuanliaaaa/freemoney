from rest_framework import serializers
from entity.models import AddMoney, SubMoney

class AddMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddMoney
        fields = '__all__'

class SubMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMoney
        fields = '__all__'
