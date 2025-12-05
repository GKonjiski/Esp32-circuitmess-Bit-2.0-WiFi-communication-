from Bit import *
import network
import socket




internet=False
data =None
tekst="Begin"
conn=None
PORT=1234
s=None
beep=0

begin()

#Opening display
display.fill(Display.Color.Red) 
#display.text(f"", 10 ,10, Display.Color.Green)
display.commit()


def internet_fun():
    global internet, conn, addr,s
    display.fill(Display.Color.Navy)
    display.text(f"Connecting", 10 ,10, Display.Color.Green)
    connect_fun()
    display.commit()
    if s is None:
        try:
        
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', PORT))
            s.listen(1)

            print("Waiting for connection", PORT)

            conn, addr = s.accept()
            print("Connected to", addr)
            internet=True
        except OSError:
            pass



def display_fun():
    global tekst
    global internet   
    display.fill(Display.Color.Navy)
    display.text(f"{tekst}", 10 ,10, Display.Color.Green)
    if internet:
        display.text(f"I", 2 ,2, Display.Color.Green)
        if tekst=="Beep":
            beep_fun()
        
    display.commit()
    

def connect_fun():
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to wifi")
        wlan.connect("WIFI-SSID", "WIFI-PASSWORD")
        
    if wlan.isconnected():
        print("Connected")
        print(wlan.ifconfig())
        
def communication_fun():
    global data, tekst, conn
    
    
    
    if internet:
        try:
            conn.setblocking(False)
            data = conn.recv(1024)
            if not data:
                print("Nothing was sent")
                
                
        except:
            pass
        if data:
            tekst = data.decode().strip()
            print("Recived:", tekst)
            
            #conn.send(("You sent: " + tekst + "\n").encode())
            data=None
        
def beep_fun():
    global tekst
    global beep
    if tekst == "Beep":
        piezo.tone(440, 20)
        tekst="change"
        print(tekst)
        
def A_func():
    global conn
    if internet:
        conn.send(("You pressed A").encode())
    
        
               

#Buttons
#buttons.on_press(Buttons.Left, Left )
#buttons.on_press(Buttons.Right, Right)
#buttons.on_press(Buttons.Up, Up)
#buttons.on_press(Buttons.Down, Down)
buttons.on_press(Buttons.A, A_func)
#buttons.on_press(Buttons.B, B)
buttons.on_press(Buttons.C, internet_fun)   


    
while True:
    buttons.scan()
    if internet:
        communication_fun()
    display_fun()



        
    
