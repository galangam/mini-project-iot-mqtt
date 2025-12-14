import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "digitalskola/iot/room-monitoring"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

rooms = ["kelas_1", "kelas_2", "lab_komputer", "server_room"]

print("Publisher room monitoring berjalan...")

while True:
    data = {
        "room": random.choice(rooms),
        "energy_usage_watt": round(random.uniform(100, 800), 2),
        "motor_status": random.choice(["ON", "OFF"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    payload = json.dumps(data)
    client.publish(TOPIC, payload)

    print("Data terkirim:", payload)
    time.sleep(5)
