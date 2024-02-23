from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .models import Legislator
from .models import Vote
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


class BillDetailsView(APIView):
    def get(self, request, bill_id):
        try:
            bill = Bill.get(id=bill_id)
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)
        supporters = self.count_supporters(bill)
        opposers = self.count_opposers(bill)
        sponsor = self.get_bill_sponsor(bill)
        data = {
            'id': bill.id,
            'title': bill.title,
            'supporters': supporters,
            'opposers': opposers,
            'sponsor': sponsor,
        }
        return Response(data)

    def count_supporters(self, bill):
        vote_ids = [vote.id for vote in Vote.all() if vote.bill_id == bill.id]
        print(vote_ids)
        supporters = []
        for vote_id in vote_ids:
            supporters.extend(VoteResult.filter(vote_id=vote_id, vote_type=1))
        return len(supporters)

    def count_opposers(self, bill):
        vote_ids = [vote.id for vote in Vote.all() if vote.bill_id == bill.id]
        opposers = []
        for vote_id in vote_ids:
            opposers.extend(VoteResult.filter(vote_id=vote_id, vote_type=2))
        return len(opposers)

    def get_bill_sponsor(self, bill):
        sponsor_id = bill.sponsor_id
        try:
            sponsor = Legislator.get(id=sponsor_id)
        except ValueError:
            return None
        return sponsor.name
