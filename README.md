Correr servidor en docker

sudo docker run -it -p 1884:1884 -p 9091:9091 -d -v /home/leo/mosquitto/mos.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto:1.4.8# front-sensores
