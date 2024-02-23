from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .models import Legislator
from .models import Vote
from .models import VoteResult
from .serializers import BillSerializer
from .serializers import LegislatorSerializer


class DetailViewMixin:
    def _count_supporters(self):
        return self._count_votes_by_type(vote_type=1)

    def _count_opposers(self):
        return self._count_votes_by_type(vote_type=2)

    def _count_votes_by_type(self, vote_type):
        raise NotImplementedError('`_count_votes_by_type()` must be implemented.')


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


class LegislatorDetailView(DetailViewMixin, APIView):
    legislator = None

    def get(self, request, legislator_id):
        try:
            self.legislator = Legislator.get(id=legislator_id)
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)

        supporters = self._count_supporters()
        opposers = self._count_opposers()

        data = {
            'id': self.legislator.id,
            'name': self.legislator.name,
            'supported': supporters,
            'opposed': opposers,
        }

        return Response(data)

    def _count_votes_by_type(self, vote_type):
        return len(VoteResult.filter(legislator_id=self.legislator.id, vote_type=1))


class BillDetailsView(DetailViewMixin, APIView):
    bill = None

    def get(self, request, bill_id):
        try:
            self.bill = Bill.get(id=bill_id)
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)
        supporters = self._count_supporters()
        opposers = self._count_opposers()
        sponsor = self._get_bill_sponsor()
        data = {
            'id': self.bill.id,
            'title': self.bill.title,
            'supporters': supporters,
            'opposers': opposers,
            'sponsor': sponsor,
        }
        return Response(data)

    def _get_vote_ids(self):
        return [vote.id for vote in Vote.all() if vote.bill_id == self.bill.id]

    def _get_bill_sponsor(self):
        sponsor_id = self.bill.sponsor_id
        try:
            sponsor = Legislator.get(id=sponsor_id)
        except ValueError:
            return None
        return sponsor.name

    def _count_votes_by_type(self, vote_type):
        vote_ids = self._get_vote_ids()
        votes = []
        for vote_id in vote_ids:
            votes.extend(VoteResult.filter(vote_id=vote_id, vote_type=vote_type))
        return len(votes)
