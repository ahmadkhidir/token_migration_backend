import datetime
from django.db import models


class DataModel(models.Model):
    file = models.FileField(upload_to='')
    modified = models.DateTimeField(auto_now=True)
    EXPIRE_AFTER = datetime.timedelta(days=1)


class WalletListModel(models.Model):
    file = models.ImageField(upload_to='wallet', max_length=100)
    name = models.CharField(max_length=100)