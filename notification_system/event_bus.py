import os
import redis
import json

class EventBus:
    def __init__(self):
        host = os.getenv("REDIS_HOST","localhost")
        try:
            self.redis = redis.Redis(host=host, port=6379, db=0, decode_responses=True)
            self.redis.ping() # Prueba la conexión al iniciar
            print(f"EventBus (PID: {os.getpid()}) conectado exitosamente a Redis en: {host}")
        except Exception as e:
            raise

        self.pubsub = self.redis.pubsub(ignore_subscribe_messages=True)
        #self.pubsub = self.redis.pubsub()


    def publish(self, channel:str, data:dict):
        message = json.dumps(data)
        self.redis.publish(channel, message)

    def subscribe(self,channel:str):
        self.pubsub.subscribe(channel)
        print(f"EventBus subscribed to channel: {channel}")
        print(f"EventBus (PID: {os.getpid()}) suscrito al canal: {channel}")

    def listen(self):
        for message in self.pubsub.listen():
            # Filtramos solo los mensajes de datos, no los de control
            #if message['type'] == 'message':
            data = json.loads(message['data'])
            yield data


event_bus = EventBus()
