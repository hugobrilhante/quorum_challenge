import os.path
from pathlib import Path

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .models import Legislator
from .parsers import CSVParser
from .serializers import BillSerializer
from .serializers import LegislatorSerializer

BASE_DIR = Path(__file__).resolve().parent


class LegislatorListView(APIView):
    def get(self, request):
        data = CSVParser(os.path.join(BASE_DIR, 'data/legislators.csv')).get_data()
        legislators = [Legislator(**legislator) for legislator in data]
        serializer = LegislatorSerializer(legislators, many=True)
        return Response(serializer.data)


class BillListView(APIView):
    def get(self, request):
        data = CSVParser(os.path.join(BASE_DIR, 'data/bills.csv')).get_data()
        bills = [Bill(**bill) for bill in data]
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)
