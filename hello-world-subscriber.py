import time as t
import json
from mqttbrokers.AWSIoTV1 import AWSIoTV1Client
from mqttbrokers.AWSIoTV2 import AWSIoTV2Client
from mqttbrokers.paho_client import PAHOClient


def on_message(msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def run():
    TOPIC = "test/testing"
    # uncomment the following line to use AWSIoTV1Client
    # client = AWSIoTV1Client()
    # uncomment the following line to use AWSIoTV2Client
    # client = AWSIoTV2Client()
    # uncomment the following line to use PAHOClient
    client = PAHOClient()
    client.setup()
    client.connect()
    client.subscribe(TOPIC,on_message)
    client.loop_forever()


if __name__ == '__main__':
    run()