import random
from mqttbrokers.mqtt_client import MQTT_CLIENT
from paho.mqtt import client as paho_mqtt_client

class PAHOClient(MQTT_CLIENT):

    def setup(self):
        super().setup()
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{random.randint(0, 1000)}'
        username = 'emqx'
        password = 'public'
        self.client = paho_mqtt_client.Client(client_id)
        self.client.username_pw_set(username, password)
        

    def connect(self):
        broker = 'broker.emqx.io'
        port = 1883
        self.client.connect(broker, port)

    def disconnect(self):
        self.client.disconnect()

    def publish(self,topic:str,payload:str, QoS: int = 0):
        self.client.publish(topic, payload=payload, qos=QoS) 

    def subscribe(self, topic, callback:callable, QoS=1, options=None, properties=None):
        self.client.subscribe(topic, qos=QoS)
        def on_message(client, userdata, msg):
            callback(msg)
        self.client.on_message = on_message

    def loop_forever(self, timeout: float = 1.0):
        return self.client.loop_forever(timeout)