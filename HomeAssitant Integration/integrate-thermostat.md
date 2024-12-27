mqtt:

  climate:
      name: "MQTT Thermostat"
      unique_id: "mqtt_thermostat_001"
      modes:
        - "off"
        - "heat"
        - "cool"
        - "auto"
      current_temperature_topic: "home/thermostat/state"
      current_temperature_template: "{{ value_json.current_temperature }}"
      temperature_command_topic: "home/thermostat/set_temperature"
      temperature_state_topic: "home/thermostat/state"
      temperature_state_template: "{{ value_json.set_temperature }}"
      mode_command_topic: "home/thermostat/mode/set"
      mode_state_topic: "home/thermostat/state"
      mode_state_template: "{{ value_json.mode }}"
      min_temp: 16
      max_temp: 30
      temp_step: 0.5