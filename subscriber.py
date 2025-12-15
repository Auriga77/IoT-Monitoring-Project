import paho.mqtt.client as mqtt

# Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "sesi20/iot/monitoring"

def on_connect(client, userdata, flags, rc):
    print("Subscriber connected to Broker!")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received from {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Blocking call that processes network traffic and callbacks
print("Waiting for messages...")
client.loop_forever()