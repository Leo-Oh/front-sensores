# coding=utf-8

import paho.mqtt.client as paho
import sys
from sensor import Sensor
import time


broker="34.94.79.113"
#broker="127.0.0.1"
port= 1884

def on_publish(client,userdata,result):            
    print("Published ->",client._client_id,"\n")
    pass

# Temperature
def temperature_room1(accion = 0):

    temperature= paho.Client("Temperature-room1")                       
    temperature.on_publish = on_publish
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/room1", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish("home/temperature/room1", "--" )
            time.sleep(5)


def temperature_room2(accion = 0):
    
    temperature= paho.Client("Temperature-room2")                      
    temperature.on_publish = on_publish 
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/room2", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish("home/temperature/room2", "--")
            time.sleep(5)

def temperature_bathroom(accion = 0):

    temperature= paho.Client("Temperature-bathroom")                       
    temperature.on_publish = on_publish                         
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/bathroom", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish("home/temperature/bathroom", "--")
            time.sleep(5)


def temperature_kitchen(accion = 0):

    temperature= paho.Client("Temperature-kitchen")                        
    temperature.on_publish = on_publish                     
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/kitchen", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish("home/temperature/kitchen", "--")
            time.sleep(5)

def temperature_livingroom(accion = 0):

    temperature= paho.Client("Temperature-livingroom")                       
    temperature.on_publish = on_publish                       
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/livingroom", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish("home/temperature/livingroom", "--")
            time.sleep(5)


def temperature_garden(accion = 0):

    temperature= paho.Client("Temperature-garden")                       
    temperature.on_publish = on_publish                
    temperature.connect(broker,port)

    if(accion == 1):
        while True:
            temperature.publish("home/temperature/garden", Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            temperature.publish("home/temperature/garden", "--")
            time.sleep(5)

# Humidity
def humidity_room1(accion = 0):

    humidity= paho.Client("Humidity-room1")                       
    humidity.on_publish = on_publish
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/room1", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/room1", "--")
            time.sleep(5)


def humidity_room2(accion = 0):
    
    humidity= paho.Client("Humidity-room2")                      
    humidity.on_publish = on_publish 
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/room2", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/room2", "--")
            time.sleep(5)

def humidity_bathroom(accion = 0):

    humidity= paho.Client("Humidity-bathroom")                       
    humidity.on_publish = on_publish                         
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/bathroom", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/bathroom", "--")
            time.sleep(5)


def humidity_kitchen(accion = 0):

    humidity= paho.Client("Humidity-kitchen")                        
    humidity.on_publish = on_publish                     
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/kitchen", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/kitchen", "--")
            time.sleep(5)


def humidity_livingroom(accion = 0):

    humidity= paho.Client("Humidity-livingroom")                       
    humidity.on_publish = on_publish                       
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/livingroom", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/livingroom", "--")
            time.sleep(5)


def humidity_garden(accion = 0):

    humidity= paho.Client("Humidity-garden")                       
    humidity.on_publish = on_publish                
    humidity.connect(broker,port)

    if(accion == 1):
        while True:
            humidity.publish("home/humidity/garden", Sensor.Sensor.generate_value(0.01,1.99,75,99.99))
            time.sleep(5)

    if(accion == 0):
        while True:
            humidity.publish("home/humidity/garden", "--")
            time.sleep(5)


# Air
def air_room1(accion = 0):

    air= paho.Client("air-room1")                       
    air.on_publish = on_publish
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/room1", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish("home/air/room1", "--")
            time.sleep(5)


def air_room2(accion = 0):
    
    air= paho.Client("air-room2")                      
    air.on_publish = on_publish 
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/room2", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish("home/air/room2", "--")
            time.sleep(5)

def air_bathroom(accion = 0):

    air= paho.Client("air-bathroom")                       
    air.on_publish = on_publish                         
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/bathroom", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish("home/air/bathroom", "--")
            time.sleep(5)


def air_kitchen(accion = 0):

    air= paho.Client("air-kitchen")                        
    air.on_publish = on_publish                     
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/kitchen", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish("home/air/kitchen", "--")
            time.sleep(5)

def air_livingroom(accion = 0):

    air= paho.Client("air-livingroom")                       
    air.on_publish = on_publish                       
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/livingroom", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish("home/air/livingroom", "--")
            time.sleep(5)


def air_garden(accion = 0):

    air= paho.Client("air-garden")                       
    air.on_publish = on_publish                
    air.connect(broker,port)

    if(accion == 1):
        while True:
            air.publish("home/air/garden", Sensor.Sensor.generate_value(0.01,0.99,400,500))
            time.sleep(5)

    if(accion == 0):
        while True:
            air.publish("home/air/garden", "--")
            time.sleep(5)

