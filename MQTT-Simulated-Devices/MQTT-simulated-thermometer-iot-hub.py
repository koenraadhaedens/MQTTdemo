import paho.mqtt.client as mqtt
import time
import random
import ssl
import certifi  # Add this import

# Azure IoT Hub details
broker = "khd-iothubdemo1.azure-devices.net"
port = 8883  # IoT Hub requires secure MQTT communication
device_id = "demothermostat"
shared_access_key = "stgkB/pCDmHrLM8vE4WtXyWOkoIjuDBTVpVQgUzu33c="  # Replace with your Shared Access Key

# MQTT topic for IoT Hub
topic = f"devices/{device_id}/messages/events/"  # IoT Hub requires this specific topic format

# Create an MQTT client instance
client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

# Set the username and password
username = f"{broker}/{device_id}/?api-version=2021-04-12"
client.username_pw_set(username, password=shared_access_key)

# Configure TLS/SSL
client.tls_set(ca_certs=certifi.where(), cert_reqs=ssl.CERT_REQUIRED)  # Use certifi for CA certificates

# Connect to the IoT Hub
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Azure IoT Hub")
    else:
        print(f"Connection failed with error code {rc}")

client.on_connect = on_connect
client.connect(broker, port)

try:
    while True:
        # Simulate temperature sensor data
        temperature = random.uniform(20.0, 25.0)  # Random temperature value
        payload = f'{{"temperature": {temperature:.2f}}}'  # JSON payload
        client.publish(topic, payload)
        print(f"Published: {payload} to {topic}")
        time.sleep(5)  # Publish every 5 seconds
except KeyboardInterrupt:
    print("Stopping simulation.")
    client.disconnect()
