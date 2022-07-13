import csv
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from v1.cmc import csv_to_data, data, data_to_csv, data_to_csv_dj, fetch_crypto_data
from django.core.files.base import ContentFile, File
from django.utils import timezone


from v1.models import DataModel


class DataAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        q = data()
        r = csv_to_data(q.file)
        return Response(r)
