from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from v1.cmc import csv_to_data, data


from v1.models import WalletListModel
from v1.serializers import WalletListSerializer


class DataAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        q = data()
        r = csv_to_data(q.file)
        return Response(r)


class WalletListView(generics.ListCreateAPIView):
    queryset = WalletListModel.objects.all()
    serializer_class = WalletListSerializer