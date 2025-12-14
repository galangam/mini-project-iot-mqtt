import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "digitalskola/iot/room-monitoring"

def on_connect(client, userdata, flags, rc):
    print("Terhubung ke broker, kode:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Data diterima:", msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()

