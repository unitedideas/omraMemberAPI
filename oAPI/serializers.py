from rest_framework import serializers
from .models import Rider


class RiderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rider
        fields = ('id', 'url', 'firstName', 'lastName', 'memberNumber', 'expirationDate', 'active')
