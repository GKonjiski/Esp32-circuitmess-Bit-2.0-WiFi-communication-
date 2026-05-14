# ESP32 WiFi Communication — CircuitMess Bit 2.0

Send and receive strings over WiFi between an ESP32 and any device (Android, PC, etc.) using a simple TCP socket connection.

---

## Hardware

- [CircuitMess Bit 2.0](https://circuitmess.com/) with integrated ESP32
- Any WiFi-enabled device to connect to it (phone, PC, tablet)

---

## How It Works

The ESP32 connects to your local WiFi network and opens a TCP socket server on **port 1234**. Any client that connects to that IP and port can exchange plain text strings with the device in both directions.

The code uses the **CircuitMess Bit library** to interface with the onboard sound chip and buttons — this is essentially a simplified wrapper around MicroPython's built-in `machine` library, adapted for the Bit 2.0 hardware.

---

## Setup

### 1. Configure WiFi credentials

Open the script and edit **line 65**:

```python
SSID = "your_network_name"
PASSWORD = "your_password"
```

### 2. Flash and run

Flash the script to your Bit 2.0 and run it. The device will connect to your WiFi network.

### 3. Get the IP address

To find the ESP32's IP address, run the following in the MicroPython REPL:

```python
# Line 69
wlan.ifconfig()
```

The first value in the returned tuple is the IP address, e.g. `192.168.1.42`.

---

## Connecting from Android

1. Install **[Serial WiFi Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_wifi_terminal)** on your Android device.
2. Open the app and create a new connection:
   - **Host:** IP address from `wlan.ifconfig()` (step 3 above)
   - **Port:** `1234`
   - **Protocol:** TCP
3. Connect — you can now send and receive strings in both directions.

---

## Connecting from a PC

You can use any TCP client, for example **netcat**:

```bash
nc <esp32-ip> 1234
```

Or any terminal app that supports raw TCP connections (e.g. PuTTY in "Raw" mode).

---

## Notes

- Both devices must be on the **same local WiFi network**.
- Only one client connection at a time is supported.
- The Bit library calls (sound, buttons) can be removed if you want to run this on a plain ESP32 without the CircuitMess hardware.

---

## Dependencies

| Library | Purpose |
|---|---|
| `network` | WiFi connection (built-in MicroPython) |
| `socket` | TCP server (built-in MicroPython) |
| `Bit` | CircuitMess Bit 2.0 hardware (buttons, sound) |

---

## License

MIT — do whatever you want with it.
