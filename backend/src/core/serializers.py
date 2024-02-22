from rest_framework import serializers


class LegislatorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class BillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    sponsor_id = serializers.IntegerField()
