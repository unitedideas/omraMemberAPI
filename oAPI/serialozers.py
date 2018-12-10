from rest_framework import serializers
from .models import MemberData


class MemberDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberData
        fields = ('id', 'url', 'firstName', 'lastName', 'memberNumber')
