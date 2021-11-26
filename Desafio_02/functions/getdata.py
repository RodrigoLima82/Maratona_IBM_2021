from paho.mqtt import client as mqtt_client
import random
import time
import json

broker    = 'iot.maratona.dev'
port      = 31666
topic     = "quanam"
client_id = 'quanam-mqtt-desafio-02-ibm'
username  = 'maratoners'
password  = 'btc-2021'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    
        with open('iot.json', 'a+') as f:
            m_decode = str(msg.payload.decode())
            r = json.dumps(m_decode,indent=7)
            f.write(r)

    client.subscribe(topic)
    client.on_message = on_message

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)


if __name__ == '__main__':
    run()