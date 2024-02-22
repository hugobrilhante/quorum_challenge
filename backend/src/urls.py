from django.contrib import admin
from django.urls import path

from src.core.views import BillListView
from src.core.views import LegislatorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislators/', LegislatorListView.as_view(), name='legislator-list'),
    path('bills/', BillListView.as_view(), name='bill-list'),
]
