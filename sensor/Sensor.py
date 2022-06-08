# coding=utf-8

import random
import time


class Sensor:
    def generate_value(val_min, val_max, previous, limit_sensor):
        while True:
            default_value= previous  # Valor inicial
            default_value_min= default_value + round(random.uniform(val_min, val_max), 2)
            default_value_max= default_value - round(random.uniform(val_min, val_max), 2)
            value_generated = round(random.uniform(default_value_min, default_value_max), 2)
            if(default_value >= limit_sensor) or (default_value_max >= limit_sensor) or value_generated >= limit_sensor:
                continue
            default_value = value_generated
            #print(value_generated)
            return value_generated