from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .models import Legislator
from .serializers import BillSerializer
from .serializers import LegislatorSerializer


class LegislatorListView(APIView):
    def get(self, request):
        legislators = Legislator.all()
        serializer = LegislatorSerializer(legislators, many=True)
        return Response(serializer.data)


class BillListView(APIView):
    def get(self, request):
        bills = Bill.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)
