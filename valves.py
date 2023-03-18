import uwebsockets.client
import sys,time
import network
from machine import Pin,ADC
from time import sleep
import _thread
import upip

import machine, time
from machine import Timer

TIMEOUT_MS = 5000 #soft-reset will happen around 5 sec

sms = ADC(Pin(34))
sms.atten(ADC.ATTN_11DB)    

def timeout_callback(t):
    try:
        print("I am in Call back")
        sleep(1)
#         if p1.off() and p2.off() and p3.off():
#             websocket.send("0")
#         elif p1.on() and p2.off() and p3.on():
#             websocket.send("1")
#         elif p1.off() and p2.on() and p3.on():
#             websocket.send("2")
#         elif p1.on() and p2.on() and p3.on():
#             wensocket.send("3")
#         
    finally:
        print("I am in Call back finally")
       

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    #upip.install("")
    
    
wlan_connect('akshu nair', 'Athvi2428')
p1= Pin(2,Pin.OUT)
p2= Pin(16,Pin.OUT)
p3= Pin(18,Pin.OUT)

uri = "wss://gtg3p8yh66.execute-api.us-east-1.amazonaws.com/production/"
websocket = uwebsockets.client.connect(uri)
#led1=Pin(2,Pin.OUT)
#led2=Pin(4,Pin.OUT)
#led3=Pin(5,Pin.OUT)
#print(websocket)

while True:
    timer = Timer(0)
    timer.init(period=TIMEOUT_MS, callback=timeout_callback)
    resp = websocket.recv()

    sms_val = sms.read()
    print (sms.read())
    if sms_val<3000:
        print("Wet")
        websocket.send("Wet")
    else:
        print("Dry")
        websocket.send("Dry")
    sleep(1)
    #three led code(drip)
    if "1" in resp:
        p1.on()
        p2.off()
        p3.on()
        print("Flow from 1")
    elif "2" in resp:
        p1.off()
        p2.on()
        p3.on()
        print("Flow from 2")
    elif "3" in resp:
        p1.on()
        p2.on()
        p3.on()
        print("Flow from 1 and 2")
    elif "0" in resp:
        p1.off()
        p2.off()
        p3.off()
        print("No flow")
    else:
        p1.off()
        p2.off()
        p3.off()
        print("No data recieved")
    sleep(1)
    
    
    
    
    
    
    
#     print("Enter Command:\r")
#     mesg=input()
#     websocket.send(mesg + "\r")
    #code for purple spherein unreal
#     led1.on()
#     print("led is on")
#     sleep(1)
#     websocket.send("on")
#     led1.off()
#     print("led is off")
#     sleep(1)
#     websocket.send("off")
    
   
  
    
     
     

     #rgb color change in spehere code for unreal
#     if "ON" in resp:
#         p0.on()
#         print("Led is on")
#     elif "OFF" in resp:
#         p0.off()
#         print("Led is off")
#     else:
#         print("No data recieved")
#         sleep(1)
