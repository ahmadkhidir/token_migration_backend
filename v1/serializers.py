from rest_framework import serializers

from v1.models import WalletListModel


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletListModel
        fields = '__all__'
