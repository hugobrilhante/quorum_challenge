from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Legislator
from .serializers import LegislatorSerializer


class LegislatorListView(APIView):
    def get(self, request):
        legislators = []
        for i in range(1, 4):
            legislator = Legislator(id=i, name=f'Legislator {i}')
            legislators.append(legislator)
        serializer = LegislatorSerializer(legislators, many=True)
        return Response(serializer.data)
