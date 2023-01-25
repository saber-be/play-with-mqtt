from __future__ import annotations
from abc import ABC

class MQTT_CLIENT(ABC):
    __slots__= ['client']
    def setup(self):
        print(f"Setup {self.__class__.__name__} client")

    def connect(self):
        pass

    def disconnect(self):
        pass

    def publish(self,topic:str,payload:str, QoS: int = 1):
        pass
    
    def subscribe(self, topic, QoS=1, options=None, properties=None):
        pass

