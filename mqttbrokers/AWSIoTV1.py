from mqttbrokers.mqtt_client import MQTT_CLIENT
from awscrt import io
from awsiot import mqtt_connection_builder

class AWSIoTV1Client(MQTT_CLIENT):

    def setup(self):
        super().setup()
        ENDPOINT = "a45t3eevjvrnb-ats.iot.us-east-1.amazonaws.com"
        CLIENT_ID = "4108c61856eb534a1d302d3816ba6032ba5c54dc7cfc3a3c87a9b1c290a7fc14"
        SSH_PATH = "/home/saber/python/mqtt/pubsub/ec2-1/"
        SSH_FILE_PREFIX = '4108c61856eb534a1d302d3816ba6032ba5c54dc7cfc3a3c87a9b1c290a7fc14'
        PATH_TO_CERTIFICATE = SSH_PATH + SSH_FILE_PREFIX + "-certificate.pem.crt"
        PATH_TO_PRIVATE_KEY = SSH_PATH + SSH_FILE_PREFIX + "-private.pem.key"
        PATH_TO_AMAZON_ROOT_CA_1 = SSH_PATH + "/AmazonRootCA1.pem"
        # Spin up resources
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        self.client = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERTIFICATE,
            pri_key_filepath=PATH_TO_PRIVATE_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
        

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    def publish(self,topic:str,payload:str, QoS: int = 1):
        self.client.publish(topic, payload, QoS) 