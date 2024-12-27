Here's a simple step-by-step guide to set up **Home Assistant** on a Hyper-V virtual machine:

---

### **Prerequisites**
1. A Windows PC with Hyper-V enabled.
2. A Home Assistant disk image file (`.vhdx` format). You can download it from the [Home Assistant website](https://www.home-assistant.io/installation/windows/).

---

### **Setup Procedure**

#### **1. Enable Hyper-V**
   - Press `Win + R`, type `optionalfeatures.exe`, and press Enter.
   - Check **Hyper-V** and its sub-features, then click OK.
   - Restart your computer if prompted.

---

#### **2. Download the Home Assistant `.vhdx` File**
   - Visit the [Home Assistant installation page](https://www.home-assistant.io/installation/windows/).
   - Download the **VHDX** version of the disk image.

---

#### **3. Open Hyper-V Manager**
   - Press `Win + S`, type `Hyper-V Manager`, and open it.

---

#### **4. Create a New Virtual Machine**
   1. In Hyper-V Manager, select your host machine in the left pane.
   2. In the right pane, click **New** > **Virtual Machine**.
   3. Follow the wizard:
      - **Name:** Set a name for the VM (e.g., Home Assistant).
      - **Generation:** Choose **Generation 2** (supports UEFI).
      - **Memory:** Allocate at least **2 GB** (4 GB recommended).
      - **Network:** Attach to a virtual switch (you may need to create one first in Virtual Switch Manager).
      - **Hard Disk:** Choose the option to use an existing disk and browse to select the `.vhdx` file you downloaded.

---

#### **5. Adjust Virtual Machine Settings (Optional)**
   - Open the VM's settings:
     - Under **Processor**, allocate at least 2 virtual processors.
     - Under **Network Adapter**, ensure it is connected to the correct virtual switch.

---

#### **6. Start the Virtual Machine**
   - Right-click your Home Assistant VM and select **Start**.
   - Open the **Connect** window to view the console.

---

#### **7. Access Home Assistant**
   - After the VM starts, it will display the IP address of your Home Assistant instance.
   - Open a browser on your PC and navigate to `http://<IP Address>:8123`.
   - Follow the on-screen instructions to complete the setup.

---

### **Additional Notes**
- **Snapshots:** After setting up Home Assistant, take a snapshot in Hyper-V to easily restore if needed.
- **Updates:** Update Home Assistant via its web interface after installation.
- **Add-Ons:** Configure additional Home Assistant integrations and add-ons as needed.
  
---

# Setting up the Mosquitto broker

---

### 1. **Prerequisites**
Before you begin:
- Ensure you have Home Assistant installed and running.
- Access to Home Assistant through a web browser.

---

### 2. **Install the Mosquitto Add-On**
1. Go to **Settings** > **Add-ons** > **Add-on Store** in Home Assistant.
2. Search for "Mosquitto broker" in the store.
3. Select the **Mosquitto broker** add-on and click **Install**.
4. Once installed, click **Start** to activate the broker.

---

### 3. **Configure Mosquitto Broker**
1. In the Mosquitto add-on configuration, you can adjust settings according to your network:
   - By default, it uses the Home Assistant user credentials for authentication.
   - If you need custom settings:
     - Click on the **Configuration** tab.
     - Add the configuration below as needed:
       ```yaml
       logins: [- username: hassio
                  password: myhassio]
       anonymous: false
       customize:
         active: false
         folder: mosquitto
       certfile: fullchain.pem
       keyfile: privkey.pem
       ```

   - Key settings:
     - `logins`: If empty, Home Assistant users are used for authentication.
     - `anonymous`: Set to `false` for secure connections.
     - `certfile` and `keyfile`: If using SSL, specify the certificate paths.
  
2. Save the configuration and restart the add-on.

---

### 4. **Enable MQTT Integration in Home Assistant**
1. Go to **Settings** > **Devices & Services**.
2. Click **Add Integration** and search for **MQTT**.
3. Select the MQTT integration and configure it:
   - **Broker**: `localhost` (if Mosquitto is running on the same system as Home Assistant).
   - **Port**: Default is `1883` (use `8883` for SSL).
   - **Username/Password**: Use the MQTT user created earlier.

4. Click **Submit** to complete the setup.


