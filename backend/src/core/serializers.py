from rest_framework import serializers


class LegislatorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
