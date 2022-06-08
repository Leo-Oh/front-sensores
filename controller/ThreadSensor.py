from nis import cat
from threading import Thread
import os
from controller import Topic
import requests
import json

class ThreadSensor():
    def __init__(self):

        self.hilos = []
    
        self.status = {
            "home/temperature/room1" : 0,
            "home/temperature/room2" : 0,
            "home/temperature/bathroom" : 0,
            "home/temperature/livingroom" : 0,
            "home/temperature/garden" : 0,
            "home/temperature/kitchen" : 0,

            "home/humidity/room1" : 0,
            "home/humidity/room2" : 0,
            "home/humidity/bathroom" : 0,
            "home/humidity/livingroom" : 0,
            "home/humidity/garden" : 0,
            "home/humidity/kitchen" : 0,

            "home/air/room1" : 0,
            "home/air/room2" : 0,
            "home/air/bathroom" : 0,
            "home/air/livingroom" : 0,
            "home/air/garden" : 0,
            "home/air/kitchen" : 0,
        }

    
    def controller_thread_all_sensors(self,topic,action):
        cores = os.cpu_count()
        api_url = "http://127.0.0.1:8000/api/status"

        print("---> Iniciando hilos ... <----")

        #OCUPAR SOLO LA PRIMERA VEZ PARA RELLENAR LA TABLA EN LA BASE DE DATOS
        
        #for url_topic in self.status:
        #    try:
        #        requests.post(api_url,
        #        data = json.dumps(
        #        {
        #            "topic": url_topic, 
        #            "status": self.status[str(url_topic)]
        #        }))
        #    except:
        #        print("Los datos ya se han creado")
            
        if topic == "home" or topic == "home/temperature"  or topic == "home/temperature/room1":
            self.status["home/temperature/room1"] = action
            hilo_temperature_room1 = Thread(target=Topic.temperature_room1, args=(self.status.get('home/temperature/room1'), ))
            self.hilos.append(hilo_temperature_room1) 

        if topic == "home" or topic == "home/temperature"  or topic == "home/temperature/room2":
            self.status["home/temperature/room2"] = action
            hilo_temperature_room2 = Thread(target=Topic.temperature_room2, args=(self.status.get('home/temperature/room2'), ))
            self.hilos.append(hilo_temperature_room2) 
        
        if topic == "home" or topic == "home/temperature"  or topic == "home/temperature/bathroom":
            self.status["home/temperature/bathroom"] = action
            hilo_temperature_bathroom = Thread(target=Topic.temperature_bathroom, args=(self.status.get('home/temperature/bathroom'), ))
            self.hilos.append(hilo_temperature_bathroom)
        
        if topic == "home" or topic == "home/temperature" or topic == "home/temperature/livingroom":
            self.status["home/temperature/livingroom"] = action
            hilo_temperature_livingroom = Thread(target=Topic.temperature_livingroom, args=(self.status.get('home/temperature/livingroom'), ))
            self.hilos.append(hilo_temperature_livingroom) 
        
        if topic == "home" or topic == "home/temperature" or topic == "home/temperature/garden":
            self.status["home/temperature/garden"] = action
            hilo_temperature_garden = Thread(target=Topic.temperature_garden, args=(self.status.get('home/temperature/garden'), ))
            self.hilos.append(hilo_temperature_garden)
        
        if topic == "home" or topic == "home/temperature" or topic == "home/temperature/kitchen":
            self.status["home/temperature/kitchen"] = action
            hilo_temperature_kitchen = Thread(target=Topic.temperature_kitchen, args=(self.status.get('home/temperature/kitchen'), ))
            self.hilos.append(hilo_temperature_kitchen) 

        """
        ==================================
                    HUMIDITY
        ==================================
        """

        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/room1":
            self.status["home/humidity/room1"] = action
            hilo_humidity_room1 = Thread(target=Topic.humidity_room1, args=(self.status.get('home/humidity/room1'), ))
            self.hilos.append(hilo_humidity_room1) 

        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/room2":
            self.status["home/humidity/room2"] = action
            hilo_humidity_room2 = Thread(target=Topic.humidity_room2, args=(self.status.get('home/humidity/room2'), ))
            self.hilos.append(hilo_humidity_room2) 
        
        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/bathroom":
            self.status["home/humidity/bathroom"] = action
            hilo_humidity_bathroom = Thread(target=Topic.humidity_bathroom, args=(self.status.get('home/humidity/bathroom'), ))
            self.hilos.append(hilo_humidity_bathroom)
        
        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/livingroom":
            self.status["home/humidity/livingroom"] = action
            hilo_humidity_livingroom = Thread(target=Topic.humidity_livingroom, args=(self.status.get('home/humidity/livingroom'), ))
            self.hilos.append(hilo_humidity_livingroom) 
        
        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/garden":
            self.status["home/humidity/garden"] = action
            hilo_humidity_garden = Thread(target=Topic.humidity_garden, args=(self.status.get('home/humidity/garden'), ))
            self.hilos.append(hilo_humidity_garden)
        
        if topic == "home" or topic == "home/humidity" or topic == "home/humidity/kitchen":
            self.status["home/humidity/kitchen"] = action
            hilo_humidity_kitchen = Thread(target=Topic.humidity_kitchen, args=(self.status.get('home/humidity/kitchen'), ))
            self.hilos.append(hilo_humidity_kitchen) 


        """
        ==================================
                    AIR
        ==================================
        """
        
        if topic == "home" or topic == "home/air" or topic == "home/air/room1":
            self.status["home/air/room1"] = action
            hilo_air_room1 = Thread(target=Topic.air_room1, args=(self.status.get('home/air/room1'), ))
            self.hilos.append(hilo_air_room1) 

        if topic == "home" or topic == "home/air" or topic == "home/air/room2":
            self.status["home/air/room2"] = action
            hilo_air_room2 = Thread(target=Topic.air_room2, args=(self.status.get('home/air/room2'), ))
            self.hilos.append(hilo_air_room2) 
        
        if topic == "home" or topic == "home/air" or topic == "home/air/bathroom":
            self.status["home/air/bathroom"] = action
            hilo_air_bathroom = Thread(target=Topic.air_bathroom, args=(self.status.get('home/air/bathroom'), ))
            self.hilos.append(hilo_air_bathroom)
        
        if topic == "home" or topic == "home/air" or topic == "home/air/livingroom":
            self.status["home/air/livingroom"] = action
            hilo_air_livingroom = Thread(target=Topic.air_livingroom, args=(self.status.get('home/air/livingroom'), ))
            self.hilos.append(hilo_air_livingroom) 
        
        if topic == "home" or topic == "home/air" or topic == "home/air/garden":
            self.status["home/air/garden"] = action
            hilo_air_garden = Thread(target=Topic.air_garden, args=(self.status.get('home/air/garden'), ))
            self.hilos.append(hilo_air_garden)
        
        if topic == "home" or topic == "home/air" or topic == "home/air/kitchen":
            self.status["home/air/kitchen"] = action
            hilo_air_kitchen = Thread(target=Topic.air_kitchen, args=(self.status.get('home/air/kitchen'), ))
            self.hilos.append(hilo_air_kitchen) 

        print("---> Ejecutando hilos ... <---")

        try:
            for hilo in self.hilos:
                if not hilo.is_alive():
                    hilo.start()
    
        except:
            print("Ya hay hilos corriendo")
        
        print("---> Esperando hilos... <---")
        for hilos in self.hilos:
            hilo.join()
