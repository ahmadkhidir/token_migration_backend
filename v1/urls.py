from django.urls import path
from v1.views import DataAPIView

app_name = 'v1'

urlpatterns = [
    path('data/', DataAPIView.as_view(), name='data')
]
