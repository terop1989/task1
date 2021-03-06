#!/usr/bin/env python3

import time
import random
import threading

import requests

endpoints = ('one', 'two', 'three', 'four')
service = "http://flask01.terop-kuber.com"


def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get(service+'/'+target, timeout=1)

        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.setDaemon(True)
        thread.start()

    while True:
        time.sleep(500)
