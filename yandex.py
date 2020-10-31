import requests
import json

TOKEN = ''

def path_verif(path):
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    params = {'path': path}
    headers = {'Authorization': TOKEN}
    resp2 = requests.get(url, params=params, headers=headers)
    return resp2


def directory(path):
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    params = {'path': path}
    headers = {'Authorization': TOKEN}
    resp = requests.put(url, params=params, headers=headers)
    verif = path_verif(path)
    verif2 = str(verif)
    resp2 = str(resp)
    answer = [verif2,resp2]
    return answer


if __name__ == "__main__":
    path = input('Введите название папки: ')
    directory(path)

