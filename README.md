
Esp32 (circuitmess Bit 2.0) WiFi communication.
This conde enables you to send strings from esp32 to android phone (or any other device) and reverse. 
I used esp32 integrated into circuitmess Bit 2.0, thats why i used their Bit library to control sound chip and buttons. But this is basically simpler version of machine library. 
Add your WiFi SSID and password on line 65. 
On Android it should work with Serial WiFi terminal app, just input ip that you can get with wlan.ifconfig() on line 69 and port number 1234.
