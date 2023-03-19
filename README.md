# Remote Monitoring and Management of Drip Irrigation using Digital Twin Technology
## Problem Statement
 We aim to provide farmers and householders the comfort of monitoring and managing their Drip Irrigation systems easier even from areas that might be kilometers apart by making use of Digital Twin Technology.

## Solution
+ We basically can create a 3D model of the whole irrigation system in a virtual world using Unreal Engine.
+ Unreal engine makes it easy to vizualize the activites and events that could be done in the real world.
  * Regulating the Water flow
  * Virtual Valves ON/OFF
 
 ![img8](https://user-images.githubusercontent.com/120260992/226200310-68681c62-7283-4ec0-b2f9-e7e76e499c9e.jpg)

 
+ Using Websockets provided by Amazon web services(AWS), the communication between the virtual and real world is initiated.
+ In the real world, the indication of the water flow on observing the soil moisture is initiated by ESP32.
+ On providing the inputs in the form of keypress in the virtual model using unreal will be indicating the ESP32 to switch on the valves in the real world through websockets.
+ ESP32 board is resposible for conytolling the differenrt components in the real world.
  * Soil Moisture
  * Physical Valves
  * Pump stations
+ Soil Moisture which is detected via ESP 32 can be monitored in the virtual world which is sent by the IOT device.

## Workflow

![img1](https://user-images.githubusercontent.com/120260992/226194771-b0c8c033-d0ba-4f13-9549-7cb2bf7e5d2f.jpg)
#### The position of the valves and the soil moisture is indicated by the ESP32 to unreal and the virtual switches are triggered , the prototype can be controlled respectively.
  ## Unreal Engine
  + 3D model of the drip irrigation system can be represented as per our convenience.
  + The core idea for this model is to represent 4 states of the system, and accordingly the states represented at the virtual end  and the real world.
  + I hav created 3 valves in the real world, that can be manipulated by the keypresses at the virtual end.
  + A Spherical shaped model is created which changes the color when each key is pressed.
  + Red represents no flow of water .
  + Green repesents the flow of water from all the valves.
  + Yellow represents the flow of water from valves 1 and 2.
  + Blue represents the flow of water from valve 2 and 3.
  + On the top left of the screen, soil moisture can be indicated to be dry or wet through a pop up message from the sensors at the real world.
  
  ![img2](https://user-images.githubusercontent.com/120260992/226198001-5c0f4a9e-6f5b-455e-8ff6-25f992986758.jpg)

## Amazon web Sockets
+ Unreal engine is connected to AWS with the help of AWS link which can be also used un IoT devices.
![img3](https://user-images.githubusercontent.com/120260992/226198188-201883f8-7a83-4739-bf64-a8cf3aee7c1e.png)

 + Creating lambda functions and DynamoDB table:
      *   This template to create a Amazon DynamoDB table to store your app's client IDs. 
      *    Lambda functions that update your client connections in DynamoDB and handle sending            messages to connected clients.
 + Create a WebSocket API:
      * A WebSocket API to handle client connections and route requests to the Lambda functions.
 + Test your API:
      * Testing your API to make sure that it works correctly. Use the wscat command to connect to the API.
 + Clean up:
      * To prevent unnecessary costs, delete the resources that you created.
      
  Below is the link to create your own websocket api to access all the services provided by AWS.
  
 https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html
 
 ## ESP 32
 
 + With the help of ESP32 the real-world components can be controlled.
 + The pins of the board are connected to the relays of the valves.
 +  We use Thonny for manipulating the operations on ESP32 such as:
       *  Soil Moisture check via sensor
       *  LED Blink
       * Buzzer
       * UltaSonic sensor
       * OlED Display
  
 ![img6](https://user-images.githubusercontent.com/120260992/226199623-f824cccc-da85-403a-b6d9-8ca1e7f34f2b.png)
![img7](https://user-images.githubusercontent.com/120260992/226199625-59ce578c-7a95-44b8-bc86-31cd1dab314d.png)
 + Soil Mositure is checked after every few seconds and sent back to the Unreal engine to display as a popup message if the soil gets dry.
 
 
 ![img4](https://user-images.githubusercontent.com/120260992/226199788-0d608e7e-d19f-4bad-a605-b9f11c0db12e.jpg)

 ![img5](https://user-images.githubusercontent.com/120260992/226199795-683230af-25c1-41e9-b7a7-ac1299369567.jpg)

 Author: C.Akshitha Nair
 
 
 
  
