from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from controller.ThreadSensor import ThreadSensor


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret!"

socketio = SocketIO(app,cors_allowed_origins="*")

"""
    ===========================================
            Here tenderized the screens
    ===========================================
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/air')
def air():
    return render_template('air.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/log')
def log():
    return render_template('log.html')

"""
    ===========================================
                Here conect the front 
                    with the sensors
    ===========================================
"""
@socketio.on('front-back-home')
def home(msg):
    print("====== [home] =====")
    print("Action:",msg)
    print("================================")
    controller_thread.controller_thread_all_sensors("home",msg)

"""
    ****************************************************************
                        Temperature ARE HERE
    ****************************************************************
"""

controller_thread  = ThreadSensor()

@socketio.on('front-back-home-temperature-room1')
def home_temperature_room1(msg):
    print("====== [home-temperature-room1] =====")
    print("Action:",msg)
    print("================================")
    controller_thread.controller_thread_all_sensors("home/temperature/room1",msg)


@socketio.on('front-back-home-temperature-room2')
def home_temperature_room2(msg):
    print("====== [home-temperature-room2] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/temperature/room2",msg)

@socketio.on('front-back-home-temperature-bathroom')
def home_temperature_bathroom(msg):
    print("====== [home-temperature-bathroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/temperature/bathroom",msg)

@socketio.on('front-back-home-temperature-kitchen')
def home_temperature_kitchen(msg):
    print("====== [home-temperature-kitchen] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/temperature/kitchen",msg)

@socketio.on('front-back-home-temperature-garden')
def home_temperature_garden(msg):
    print("====== [home-temperature-garden] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/temperature/garden",msg)


@socketio.on('front-back-home-temperature-livingroom')
def home_temperature_livingroom(msg):
    print("====== [home-temperature-livingroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/temperature/livingroom",msg)


"""
    ****************************************************************
                        HUMIDITY ARE HERE
    ****************************************************************
"""
@socketio.on('conect')
def conect():
    print("Conectado")

@socketio.on('front-back-home-humidity-room1')
def home_humidity_room1(msg):
    print("====== [home-humidity-room1] =====")
    print("Action:",msg)
    print("================================")
    controller_thread.controller_thread_all_sensors("home/humidity/room1",msg)


@socketio.on('front-back-home-humidity-room2')
def home_humidity_room2(msg):
    print("====== [home-humidity-room2] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/humidity/room2",msg)

@socketio.on('front-back-home-humidity-bathroom')
def home_humidity_bathroom(msg):
    print("====== [home-humidity-bathroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/humidity/bathroom",msg)

@socketio.on('front-back-home-humidity-kitchen')
def home_humidity_kitchen(msg):
    print("====== [home-humidity-kitchen] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/humidity/kitchen",msg)

@socketio.on('front-back-home-humidity-garden')
def home_humidity_garden(msg):
    print("====== [home-humidity-garden] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/humidity/garden",msg)


@socketio.on('front-back-home-humidity-livingroom')
def home_humidity_livingroom(msg):
    print("====== [home-humidity-livingroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/humidity/livingroom",msg)




"""
    ****************************************************************
                        AIR ARE HERE
    ****************************************************************
"""


@socketio.on('front-back-home-air-room1')
def home_air_room1(msg):
    print("====== [home-air-room1] =====")
    print("Action:",msg)
    print("================================")
    controller_thread.controller_thread_all_sensors("home/air/room1",msg)


@socketio.on('front-back-home-air-room2')
def home_air_room2(msg):
    print("====== [home-air-room2] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/air/room2",msg)

@socketio.on('front-back-home-air-bathroom')
def home_air_bathroom(msg):
    print("====== [home-air-bathroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/air/bathroom",msg)

@socketio.on('front-back-home-air-kitchen')
def home_air_kitchen(msg):
    print("====== [home-air-kitchen] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/air/kitchen",msg)

@socketio.on('front-back-home-air-garden')
def home_air_garden(msg):
    print("====== [home-air-garden] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/air/garden",msg)


@socketio.on('front-back-home-air-livingroom')
def home_air_livingroom(msg):
    print("====== [home-air-livingroom] =====")
    print("Action:",msg)
    controller_thread.controller_thread_all_sensors("home/air/livingroom",msg)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9096", debug=True)
