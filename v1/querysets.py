from django.utils import timezone
from django.db import models
from django.core.files.base import ContentFile, File

from v1.cmc import AWS_S3, data_to_csv, data_to_csv_dj, fetch_crypto_data


class DataQuerySet(models.QuerySet):
    def data(self):
        ctime = timezone.now()
        expire = self.model.EXPIRE_AFTER
        ins = self.last()
        print('>>', ins)
        if not ins:
            print('eeeeewwww')
            crypto_data = fetch_crypto_data()
            file = data_to_csv(crypto_data)
            try:
                ins = self.model.objects.create(file='crypto.csv')
                ins.file = File(file)
                return ins
            except Exception as e:
                raise ValueError(f'unable to create file and {e}')

        print(ins.modified, ctime, expire)
        print(ins.modified > (ctime - expire))
        if ins.modified > (ctime - expire):
            print('osh')
            return ins
        else:
            print('hmm')
            crypto_data = fetch_crypto_data()
            file = data_to_csv(crypto_data)
            try:
                ins.file = file
            except Exception as e:
                raise ValueError(f'unable to create file and {e}')
            return ins
