import requests
import time


# define a class called Thingspeak
class Thingspeak(object):                      

    def __init__(self, write_api_key = None, read_api_key=None, channel_id=0):

        """

        :param write_key:  takes a string of write api key
        :param timer: can take integer values
        """

        # self.url = 'https://api.thingspeak.com/update?api_key='
        # self.read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

        self.write_key = write_api_key
        self.channel_id = channel_id
        self.read_api_key = read_api_key

        # Private Var cannot change
        self.__url = 'http://api.thingspeak.com/update?api_key'
        self.__read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

    def read_cloud(self, result=2):
        try:
            """
            :param result: how many data you want to fetch accept interger
            :return: Two List which contains Sensor data
            """

            URL_R = self.__read_url
            read_key = self.read_api_key
            header_r = '&results={}'.format(result)

            new_read_url = URL_R + read_key + header_r

            data = requests.get(new_read_url).json()

            field1 = data['feeds']

            for x in field1:
                # convert string to float
                value = float(x['field1'])
                # give condition if value is greater than 0
                if value > 0:
                    print(f"Sucessfully received data : {value} from Thingspeak")
                time.sleep(2) # delay for 2 seconds for each iteration
        except:
            print("Read from cloud failed!!!")


# Main Loop
def main():
    cue = input(str("Y to Start: "))
    cue = cue.lower()
    if cue == "y":
        while True:
            write_key = "B384P8GG2YUIPAXM"
            read_key = "MG1800QAR6X7QCE6"
            channel_id = 2172873

            # call the thingspeak class
            # pass in your write API, read API, and channel ID
            ts = Thingspeak(write_key, read_key, channel_id)
            ts.read_cloud()

    print('Program exited...')
        



# check if running as module or script
# good practice to do in the Python Programming Language
if __name__ == "__main__":
    main()