from django.contrib import admin
from django.urls import path

from src.core.views import BillDetailsView
from src.core.views import BillListView
from src.core.views import LegislatorDetailView
from src.core.views import LegislatorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislators/', LegislatorListView.as_view(), name='legislator-list'),
    path('legislators/<int:legislator_id>/', LegislatorDetailView.as_view(), name='legislator-detail'),
    path('bills/', BillListView.as_view(), name='bill-list'),
    path('bills/<int:bill_id>/', BillDetailsView.as_view(), name='bill-details'),
]
