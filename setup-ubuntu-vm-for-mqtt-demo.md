Here's a step-by-step guide to set up an MQTT message system using Mosquitto broker, Telegraf for data collection, and Grafana for data visualization on an Ubuntu VM.

### Step 1: Install Mosquitto MQTT Broker
1. **Update your package list and install Mosquitto**:
    ```bash
    sudo apt update
    sudo apt install mosquitto mosquitto-clients
    sudo mosquitto_passwd -c /etc/mosquitto/passwd hassio
    sudo nano /etc/mosquitto/mosquitto.conf
        add following lines to config. Press ctrl O and enter to save and press ctrl X to exit nano

            allow_anonymous false
            password_file /etc/mosquitto/passwd

        ```

2. **Start and enable Mosquitto service**:
    ```bash
    sudo systemctl start mosquitto
    sudo systemctl enable mosquitto
    ```

### Step 2: Install and Configure InfluxDB2

1. **Install InFluxDB2**
    ```bash
    sudo wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    sudo gpg --with-fingerprint --show-keys ./influxdata-archive_compat.key
    sudo cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    sudo echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
    sudo apt-get update
    sudo apt install influxdb2 -y
    sudo systemctl start influxdb
    sudo systemctl enable influxdb
    ```
Go to http://<your ip>:8086 to configure InfluxDB2

### Step 3: Install and Configure Telegraf
1. **Install Telegraf**:
    ```bash
    sudo apt update
    sudo apt install telegraf
    ```

2. **Configure Telegraf to collect data from Mosquitto**:
    Edit the Telegraf configuration file:
    ```bash
    sudo nano /etc/telegraf/telegraf.conf
    ```
    Add the following configuration to subscribe to MQTT topics:
    ```toml
    [[inputs.mqtt_consumer]]
      servers = ["tcp://localhost:1883"]
      topics = ["test"]
      data_format = "json"
    ```

3. **Start and enable Telegraf service**:
    ```bash
    sudo systemctl start telegraf
    sudo systemctl enable telegraf
    ```



### Summary
By following these steps, you will have set up an MQTT message system with Mosquitto broker, Telegraf for data collection, and Grafana for data visualization. This setup allows you to publish MQTT messages to the Mosquitto broker, collect them with Telegraf, and visualize the data in Grafana[2](https://www.influxdata.com/blog/MQTT-Telegraf-InfluxDB-Cloud-v3-tutorial/)[3](https://itobey.dev/connecting-telegraf-to-mosquitto-with-influxdb/)[4](https://grafana.com/tutorials/stream-metrics-from-telegraf-to-grafana/).
