import paho.mqtt.client as mqtt
import time
import random
import json
import logging

logging.basicConfig(level=logging.DEBUG)  # Enable debug logs

broker = "52.169.39.219"  # Replace with your MQTT broker address
port = 1883

# MQTT credentials
username = "hassio"  # Replace with your MQTT broker username
password = "myhassio"  # Replace with your MQTT broker password

# MQTT topics
state_topic = "home/thermostat/state"
set_temp_topic = "home/thermostat/set_temperature"
set_mode_topic = "home/thermostat/mode/set"

# Initial state
current_temperature = 22.5
set_temperature = 24.0
current_mode = "off"

# Callback for when a message is received
def on_message(client, userdata, message):
    global set_temperature, current_mode
    try:
        # Decode the payload
        payload = message.payload.decode()
        
        # Handle set temperature command (plain float or string)
        if message.topic == set_temp_topic:
            set_temperature = float(payload)
            print(f"Set temperature updated to: {set_temperature}°C")
        
        # Handle mode command (plain string)
        elif message.topic == set_mode_topic:
            current_mode = payload
            print(f"Mode updated to: {current_mode}")
    except ValueError as e:
        print(f"Error processing message: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Create MQTT client
client = mqtt.Client(client_id="ThermostatSimulator")

# Set username and password
client.username_pw_set(username, password)

# Set callback function
client.on_message = on_message

# Connect to broker
client.connect(broker, port)

# Subscribe to command topics
client.subscribe(set_temp_topic)
client.subscribe(set_mode_topic)

# Start MQTT loop in the background
client.loop_start()

try:
    while True:
        # Publish combined state as JSON
        state_payload = json.dumps({
            "current_temperature": round(current_temperature, 1),
            "set_temperature": round(set_temperature, 1),
            "mode": current_mode
        })
        client.publish(state_topic, state_payload)
        print(f"Published state: {state_payload}")
        
        # Simulate slight changes in the current temperature
        current_temperature += random.uniform(-0.1, 0.1)
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping simulation.")
    client.loop_stop()
    client.disconnect()
