# coding=utf-8

import paho.mqtt.client as paho
import sys
from sensor import Sensor
import time
import requests
import json
from datetime import datetime

broker="34.94.79.113"
#broker="127.0.0.1"
port= 1884
api_url = "http://127.0.0.1:8000/api/log"

now = datetime.now()

def on_publish(client,userdata,result):            
    print("Published ->",client._client_id,"\n")
    pass

# Temperature
def temperature_room1(accion = 0):

    temperature= paho.Client("Temperature-room1")                       
    temperature.on_publish = on_publish
    temperature.connect(broker,port)
    topic = "home/temperature/room1"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)
            print("payload: ", payload ,"fecha: ", fecha,"hora", hora )

            requests.post("http://127.0.0.1:8000/api/log",
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)


            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish(topic, "--" )
            time.sleep(5)


def temperature_room2(accion = 0):
    
    temperature= paho.Client("Temperature-room2")                      
    temperature.on_publish = on_publish 
    temperature.connect(broker,port)

    topic = "home/temperature/room2"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)
            time.sleep(5)

    if(accion == 0):
        while True:
            temperature.publish(topic, "--")
            time.sleep(5)

def temperature_bathroom(accion = 0):

    temperature= paho.Client("Temperature-bathroom")                       
    temperature.on_publish = on_publish                         
    temperature.connect(broker,port)

    topic = "home/temperature/bathroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)
            time.sleep(5)

    if(accion == 0):
        while True:
            temperature.publish(topic, "--")
            time.sleep(5)


def temperature_kitchen(accion = 0):

    temperature= paho.Client("Temperature-kitchen")                        
    temperature.on_publish = on_publish                     
    temperature.connect(broker,port)

    topic = "home/temperature/kitchen"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish(topic, "--")
            time.sleep(5)

def temperature_livingroom(accion = 0):

    temperature= paho.Client("Temperature-livingroom")                       
    temperature.on_publish = on_publish                       
    temperature.connect(broker,port)

    topic = "home/temperature/livingroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish(topic, "--")
            time.sleep(5)

def temperature_garden(accion = 0):

    temperature= paho.Client("Temperature-garden")                       
    temperature.on_publish = on_publish                
    temperature.connect(broker,port)

    topic = "home/temperature/garden"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,30.01,39.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            temperature.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            temperature.publish(topic, "--")
            time.sleep(5)

# Humidity
def humidity_room1(accion = 0):

    humidity= paho.Client("Humidity-room1")                       
    humidity.on_publish = on_publish
    humidity.connect(broker,port)

    topic = "home/humidity/room1"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)


def humidity_room2(accion = 0):
    
    humidity= paho.Client("Humidity-room2")                      
    humidity.on_publish = on_publish 
    humidity.connect(broker,port)

    topic = "home/humidity/room2"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)

def humidity_bathroom(accion = 0):

    humidity= paho.Client("Humidity-bathroom")                       
    humidity.on_publish = on_publish                         
    humidity.connect(broker,port)

    topic = "home/humidity/bathroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)


def humidity_kitchen(accion = 0):

    humidity= paho.Client("Humidity-kitchen")                        
    humidity.on_publish = on_publish                     
    humidity.connect(broker,port)

    topic = "home/humidity/kitchen"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)


def humidity_livingroom(accion = 0):

    humidity= paho.Client("Humidity-livingroom")                       
    humidity.on_publish = on_publish                       
    humidity.connect(broker,port)

    topic = "home/humidity/livingroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)


def humidity_garden(accion = 0):

    humidity= paho.Client("Humidity-garden")                       
    humidity.on_publish = on_publish                
    humidity.connect(broker,port)

    topic = "home/humidity/garden"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,1.99,75,99.99)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            humidity.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            humidity.publish(topic, "--")
            time.sleep(5)


# Air
def air_room1(accion = 0):

    air= paho.Client("air-room1")                       
    air.on_publish = on_publish
    air.connect(broker,port)

    topic = "home/air/room1"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)


def air_room2(accion = 0):
    
    air= paho.Client("air-room2")                      
    air.on_publish = on_publish 
    air.connect(broker,port)

    topic = "home/air/room2"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)

def air_bathroom(accion = 0):

    air= paho.Client("air-bathroom")                       
    air.on_publish = on_publish                         
    air.connect(broker,port)

    topic = "home/air/bathroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)


def air_kitchen(accion = 0):

    air= paho.Client("air-kitchen")                        
    air.on_publish = on_publish                     
    air.connect(broker,port)

    topic = "home/air/kitchen"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)

def air_livingroom(accion = 0):

    air= paho.Client("air-livingroom")                       
    air.on_publish = on_publish                       
    air.connect(broker,port)

    topic = "home/air/livingroom"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)


def air_garden(accion = 0):

    air= paho.Client("air-garden")                       
    air.on_publish = on_publish                
    air.connect(broker,port)

    topic = "home/air/garden"

    if(accion == 1):
        while True:
            payload = Sensor.Sensor.generate_value(0.01,0.99,400,500)
           
            fecha = '{}-{}-{}'.format(now.year,now.month,now.day) 
            hora  = '{}:{}:{}'.format(now.hour,now.minute,now.second)

            requests.post(api_url,
                data = json.dumps(
                 {
                    "topic": topic,
                    "value" : payload,
                    "date" : fecha,
                    "time" : hora,
                }))
            air.publish(topic, payload)
            time.sleep(5)
    if(accion == 0):
        while True:
            air.publish(topic, "--")
            time.sleep(5)
