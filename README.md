# ESP32 WiFi Communication — CircuitMess Bit 2.0

Send and receive strings over WiFi between a CircuitMess Bit 2.0 and any device (Android, PC, etc.) using a simple TCP socket connection.

---

## Hardware

- [CircuitMess Bit 2.0](https://circuitmess.com/) with integrated ESP32

---

## How It Works

The ESP32 acts as a **TCP server** on port `1234`. After connecting to your WiFi network, it waits for a client to connect and then exchanges plain text strings in both directions.

The code uses the **CircuitMess Bit library** (`Bit`) to interface with the onboard display, piezo buzzer, and buttons — a simplified wrapper around MicroPython's `machine` library tailored for the Bit 2.0 hardware.

---

## Setup

### 1. Configure WiFi credentials

Open `main.py` and edit **line 65**:

```python
wlan.connect("WIFI-SSID", "WIFI-PASSWORD")
```

Replace `WIFI-SSID` and `WIFI-PASSWORD` with your network name and password.

### 2. Flash and run

Flash `main.py` to your Bit 2.0 and run it. The display will turn **red** on boot.

### 3. Connect to WiFi

Press **button C** on the device. This triggers the WiFi connection and starts the TCP server. The display will show `Connecting` and then wait for an incoming client connection.

### 4. Get the IP address

The IP address is printed to the serial console once connected (line 69):

```python
print(wlan.ifconfig())
```

The first value in the output is the IP, e.g. `('192.168.1.42', ...)`.

---

## Connecting from Android

1. Install **[Serial WiFi Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_wifi_terminal)**.
2. Create a new connection:
   - **Host:** IP from `wlan.ifconfig()`
   - **Port:** `1234`
   - **Protocol:** TCP
3. Connect — you can now type strings and send them to the device, and receive messages from it.

---

## Connecting from a PC

Use netcat or any TCP client:

```bash
nc <esp32-ip> 1234
```

Or PuTTY in **Raw** mode with the same IP and port.

---

## Controls

| Button | Action |
|--------|--------|
| **C** | Connect to WiFi and start the TCP server |
| **A** | Send `"You pressed A"` to the connected client |

---

## Receiving Messages

Any string sent from the client is displayed on the Bit's screen. One special value is handled:

| Message received | Effect |
|-----------------|--------|
| `Beep` | Plays a 440 Hz tone on the piezo buzzer |

The display also shows a small `I` indicator in the top-left corner when a client is connected.

---

## Notes

- Both devices must be on the **same local WiFi network**.
- Only **one client** at a time is supported.
- If you want to use this on a plain ESP32 without CircuitMess hardware, replace all `Bit` library calls (`display`, `piezo`, `buttons`) with standard MicroPython `machine` equivalents.
- Left, Right, Up, Down, and B buttons are defined in the code but commented out — ready for you to extend.

---

## Dependencies

| Library | Purpose |
|---------|---------|
| `Bit` | CircuitMess Bit 2.0 hardware (display, buttons, piezo) |
| `network` | WiFi connection — built-in MicroPython |
| `socket` | TCP server — built-in MicroPython |

---

## License

MIT — do whatever you want with it.
