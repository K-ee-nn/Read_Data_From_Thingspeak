import requests
import time


# Thingspeak 클래스 정의
class Thingspeak(object):

    def __init__(self, write_api_key=None, read_api_key=None, channel_id=0):
        """
        :param write_key: 쓰기 API 키 문자열
        :param timer: 정수 값을 가질 수 있음
        """

        # self.url = 'https://api.thingspeak.com/update?api_key='
        # self.read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

        self.write_key = write_api_key
        self.channel_id = channel_id
        self.read_api_key = read_api_key

        # 프라이빗 변수는 변경할 수 없음
        self.__url = 'http://api.thingspeak.com/update?api_key'
        self.__read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

    def read_cloud(self, result=2):
        try:
            """
            :param result: 검색할 데이터 개수, 정수 값으로 입력
            :return: 두 개의 센서 데이터를 포함하는 리스트 반환
            """

            URL_R = self.__read_url
            read_key = self.read_api_key
            header_r = '&results={}'.format(result)

            new_read_url = URL_R + read_key + header_r

            data = requests.get(new_read_url).json()

            field1 = data['feeds']

            for x in field1:
                # 문자열을 부동 소수점으로 변환
                value = float(x['field1'])
                # 값이 0보다 크면 출력
                if value > 0:
                    print(f"Thingspeak에서 데이터를 성공적으로 받았습니다: {value}")
                time.sleep(2)  # 각 반복마다 2초 딜레이
        except:
            print("클라우드에서 읽기 실패!!!")


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
            # 쓰기 API, 읽기 API 및 채널 ID를 전달
            ts = Thingspeak(write_key, read_key, channel_id)
            ts.read_cloud()

    print('프로그램 종료...')


# 모듈로서 실행되는지 또는 스크립트로서 실행되는지 확인
if __name__ == "__main__":
    main()
