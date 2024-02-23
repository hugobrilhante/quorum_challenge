from collections import OrderedDict

from rest_framework import serializers

from src.core.models import Legislator


class BaseModelSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return instance.__dict__


class LegislatorSerializer(BaseModelSerializer):
    pass


class BillSerializer(BaseModelSerializer):
    pass
