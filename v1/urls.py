from django.urls import path
from v1 import views

app_name = 'v1'

urlpatterns = [
    path('data/', views.DataAPIView.as_view(), name='data'),
    path('wallet/', views.WalletListView.as_view(), name='wallet'),
    path('form/', views.WalletForm.as_view(), name='form'),
]
