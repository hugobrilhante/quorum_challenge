from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .models import Legislator
from .models import VoteResult
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


class LegislatorDetailView(APIView):
    def get(self, request, legislator_id):
        try:
            legislator = Legislator.get(id=legislator_id)
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)

        votes = self._get_legislator_votes(legislator)

        data = {'id': legislator.id, 'name': legislator.name, **votes}

        return Response(data)

    def _get_legislator_votes(self, legislator):
        legislator_id = legislator.id
        supported_bills = VoteResult.filter(legislator_id=legislator_id, vote_type=1)
        opposed_bills = VoteResult.filter(legislator_id=legislator_id, vote_type=2)
        return {'supported_bills': len(supported_bills), 'opposed_bills': len(opposed_bills)}
