from rest_framework import serializers

from myDashboard.api.transport_models import UniData


class UniSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniData
        fields = '__all__'
