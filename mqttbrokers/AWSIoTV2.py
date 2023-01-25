from mqttbrokers.mqtt_client import MQTT_CLIENT
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

class AWSIoTV2Client(MQTT_CLIENT):

    def setup(self):
        super().setup()
        ENDPOINT = "a45t3eevjvrnb-ats.iot.us-east-1.amazonaws.com"
        CLIENT_ID = "4108c61856eb534a1d302d3816ba6032ba5c54dc7cfc3a3c87a9b1c290a7fc14"
        SSH_PATH = "/home/saber/python/mqtt/pubsub/ec2-1/"
        SSH_FILE_PREFIX = '4108c61856eb534a1d302d3816ba6032ba5c54dc7cfc3a3c87a9b1c290a7fc14'
        PATH_TO_CERTIFICATE = SSH_PATH + SSH_FILE_PREFIX + "-certificate.pem.crt"
        PATH_TO_PRIVATE_KEY = SSH_PATH + SSH_FILE_PREFIX + "-private.pem.key"
        PATH_TO_AMAZON_ROOT_CA_1 = SSH_PATH + "/AmazonRootCA1.pem"

        self.client = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
        self.client.configureEndpoint(ENDPOINT, 8883)
        self.client.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
        

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    def publish(self,topic:str,payload:str, QoS: int = 1):
        self.client.publish(topic, payload, QoS) 