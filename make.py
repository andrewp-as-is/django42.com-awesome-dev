#!/usr/bin/env python
import requests
import os

URL = 'http://127.0.0.1:8000/awesome/awesome.json'


def save(path, data):
    path = os.path.join(path, data['slug'])
    os.makedirs(path)
    open(path + '/name.txt', 'w').write(data['name'])
    if 'description' in data:
        open(path + '/description.txt', 'w').write(data['description'])
    if 'projects' in data:
        open(path + '/projects.txt', 'w').write("\n".join(data['projects']))
    for data in data.get('collections', []):
        save(path, data)


def make():
    r = requests.get(URL)
    for data in r.json()['collections']:
        save(os.getcwd() + '/collections', data)


if __name__ == "__main__":
    make()
