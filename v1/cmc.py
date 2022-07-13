from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
from django.core.files.base import ContentFile
from v1.models import DataModel
from django.utils import timezone


def fetch_crypto_data():
    listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    info_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '715dfed8-6b87-4d78-b3c0-82c4c8f513ef',
    }
    session = Session()
    session.headers.update(headers)
    listings_parameter = {
        'start': '1',
        'limit': '100',
        'convert': 'USD'
    }
    try:
        response = session.get(listings_url, params=listings_parameter)
        data = json.loads(response.text)['data']
        ids = []
        cleaned_data = {}
        for obj in data:
            ids.append(str(obj['id']))
            item = {
                'name': obj['name'],
                'symbol': obj['symbol'],
                'rank': obj['cmc_rank'],
                'price': obj['quote']['USD']['price'],
                'percent_change': obj['quote']['USD']['percent_change_24h'],
                'volume': obj['quote']['USD']['volume_24h'],
                'market_cap': obj['quote']['USD']['market_cap'],
            }
            cleaned_data[str(obj['id'])] = item
        response = session.get(info_url, params={'id': ','.join(ids)})
        data = json.loads(response.text)['data']
        for (k, obj) in data.items():
            item = cleaned_data[str(k)]
            item['logo'] = obj['logo']
            item['url'] = obj['urls']['website'][0]
        return cleaned_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return -1


def data_to_csv(data):
    filename = 'crypto.csv'
    with open(filename, 'w+') as crypto:
        writer = csv.writer(crypto)
        header = ['name', 'symbol', 'rank', 'price',
                  'percent_change', 'volume', 'market_cap', 'logo', 'url']
        writer.writerow(header)
        for obj in data.values():
            writer.writerow(obj.values())
    return filename


def data_to_csv_dj(data):
    crypto = ContentFile(b'', 'crypto.csv')
    writer = csv.writer(crypto)
    header = ['name', 'symbol', 'rank', 'price',
              'percent_change', 'volume', 'market_cap', 'logo', 'url']
    h = ','.join(header)
    h = h.encode('ascii')
    writer.writerow(['hello world'.encode('ascii')])
    # for obj in data.values():
    #     writer.writerow(obj.values())
    crypto.seek(0, 0)
    q = crypto.read().encode('ascii')
    crypto.write(q)
    crypto.close()
    return crypto


def csv_to_data(data):
    res = []
    data.seek(0)
    file = data.readlines()
    header = file[0].decode('utf-8').strip('\n').split(',')
    for i in file[1:]:
        if i == b'\n':
            continue
        i = i.decode('utf-8').strip('\n').split(',')
        a = {}
        for j in i:
            a[header[i.index(j)]] = j
        res.append(a)
    return res


def data():
    ctime = timezone.now()
    expire = DataModel.EXPIRE_AFTER
    d = DataModel.objects.last()
    if not d:
        crypto_data = fetch_crypto_data()
        file = data_to_csv(crypto_data)
        f = open(file)
        content = ContentFile(f.read().encode('ascii'), 'crypto.csv')
        content.close()
        try:
            # Save to AWS
            ins = DataModel(file=content)
            ins.save()
            return ins
        except Exception as e:
            raise ValueError(f'unable to create file and {e}')

    if d.modified > (ctime - expire):
        return d
    else:
        crypto_data = fetch_crypto_data()
        file = data_to_csv(crypto_data)
        try:
            d.file = file
            d.save()
        except Exception as e:
            raise ValueError(f'unable to create file and {e}')
        return d
