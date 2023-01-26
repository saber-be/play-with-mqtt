import time as t
import json
from mqttbrokers.AWSIoTV1 import AWSIoTV1Client
from mqttbrokers.AWSIoTV2 import AWSIoTV2Client
from mqttbrokers.paho_client import PAHOClient

MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 30

# uncomment the following line to use AWSIoTV1Client
# client = AWSIoTV1Client()
# uncomment the following line to use AWSIoTV2Client
# client = AWSIoTV2Client()
# uncomment the following line to use PAHOClient
client = PAHOClient()
client.setup()
client.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"messages" : data}
    client.publish(TOPIC, json.dumps(message)) 
    print(f"Published: '{json.dumps(message)}' to the topic: '{TOPIC}'")
    t.sleep(0.5)
print('Publish End')
input("Press Enter to disconnect...")
client.disconnect()