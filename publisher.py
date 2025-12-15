import paho.mqtt.client as mqtt
import time
import json
import random

# Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "sesi20/iot/monitoring"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher connected to Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)

# Simulation Loop
try:
    while True:
        # Simulate sensor data
        payload = {
            "energy_kwh": round(random.uniform(10.5, 50.0), 2),
            "room_temp_c": round(random.uniform(20.0, 30.0), 1),
            "motor_rpm": random.randint(1000, 3000)
        }
        
        # Publish data
        client.publish(TOPIC, json.dumps(payload))
        print(f"Sent: {payload}")
        
        time.sleep(2) # Send every 2 seconds
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()