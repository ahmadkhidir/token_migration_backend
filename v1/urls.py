from django.urls import path
from v1.views import DataAPIView, WalletListView

app_name = 'v1'

urlpatterns = [
    path('data/', DataAPIView.as_view(), name='data'),
    path('wallet/', WalletListView.as_view(), name='wallet')
]
