from urllib import request
from urllib.request import urlopen
import threading
import json
import random
import requests
import ssl
import geocoder
import datetime
from twilio.rest import Client
from serial import Serial
import numpy as np
from Adafruit_IO import Client
import os
from os import system
import paho.mqtt.publish as publish
import sqlite3
import paho.mqtt.publish as publish
import urllib
import time


# Thingspeak 클래스 정의
class Thingspeak(object):
    def __init__(self, write_api_key=None, read_api_key=None, channel_id=0):
        """

        :param write_key: 쓰기 API 키 문자열
        :param timer: 정수값을 받을 수 있음
        """

        # self.url = 'https://api.thingspeak.com/update?api_key='
        # self.read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

        self.write_key = write_api_key
        self.channel_id = channel_id
        self.read_api_key = read_api_key

        # 비공개 변수는 변경 불가능
        self.__url = 'http://api.thingspeak.com/update?api_key'
        self.__read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

    def read_cloud(self, result=2):
        try:
            """
            :param result: 가져올 데이터 개수를 나타내는 정수값
            :return: 두 개의 리스트를 반환하여 센서 데이터를 담고 있음
            """

            URL_R = self.__read_url
            read_key = self.read_api_key
            header_r = '&results={}'.format(result)

            new_read_url = URL_R + read_key + header_r

            data = requests.get(new_read_url).json()

            field1 = data['feeds']

            for x in field1:
                # 문자열을 실수형으로 변환
                value = float(x['field1'])
                # 값이 50보다 크면 조건 충족
                if value > 50.0:
                    print(f"Thingspeak에서 성공적으로 데이터를 받았습니다 : {value}")
                time.sleep(2)  # 각 반복마다 2초 지연
        except:
            print("클라우드로부터 읽어오는 데 실패했습니다!!!")


# 메인 루프
def main():
    cue = input(str("시작하려면 Y를 입력하세요: "))
    cue = cue.lower()
    if cue == "y":
        while True:
            write_key = None
            read_key = None
            channel_id = None

            # Thingspeak 클래스 호출
            # 쓰기 API, 읽기 API, 채널 ID를 전달
            ts = Thingspeak(write_key, read_key, channel_id)
            ts.read_cloud()

    print('프로그램이 종료되었습니다...')


# 스크립트로서 실행되는지 혹은 모듈로서 실행되는지 확인
# Python 프로그래밍 언어에서 좋은 습관
if __name__ == "__main__":
    main()
