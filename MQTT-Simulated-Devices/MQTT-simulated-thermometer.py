import paho.mqtt.client as mqtt
import time
import random

# MQTT broker details
broker = "52.169.39.219"  # Replace with your broker address
port = 1883
topic = "home/sensor/temperature"
username = "hassio"  # Replace with your MQTT broker username
password = "myhassio"  # Replace with your MQTT broker password

# Create an MQTT client instance with callback_api_version
client = mqtt.Client(client_id="SensorSimulator")

# Set username and password
client.username_pw_set(username, password)

# Connect to the broker
client.connect(broker, port)

try:
    while True:
        # Simulate temperature sensor data
        temperature = random.uniform(20.0, 25.0)  # Random temperature value
        payload = f"{temperature:.2f}"
        client.publish(topic, payload)
        print(f"Published: {payload} to {topic}")
        time.sleep(5)  # Publish every 5 seconds
except KeyboardInterrupt:
    print("Stopping simulation.")
    client.disconnect()