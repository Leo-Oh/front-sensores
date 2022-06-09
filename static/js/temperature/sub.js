//var hostname = "127.0.0.1";
var hostname = "34.94.79.113";
var port = 9091;
var clientId = "sub-temperature-";
clientId += new Date().getUTCMilliseconds();;


mqttClient = new Paho.MQTT.Client(hostname, port, clientId);
mqttClient.onMessageArrived = MessageArrived;
mqttClient.onConnectionLost = ConnectionLost;
Connect();

/*Initiates a connection to the MQTT broker*/
function Connect() {
	mqttClient.connect({
		onSuccess: Connected,
		onFailure: ConnectionFailed,
	});
}

/*Callback for successful MQTT connection */
function Connected() {
	mqttClient.subscribe("home/temperature/room1");
	mqttClient.subscribe("home/temperature/room2");
	mqttClient.subscribe("home/temperature/bathroom");
	mqttClient.subscribe("home/temperature/livingroom");
	mqttClient.subscribe("home/temperature/kitchen");
	mqttClient.subscribe("home/temperature/garden");
	console.log("Connected PAHO");
}

/*Callback for failed connection*/
function ConnectionFailed(res) {
	console.log("Connect failed:" + res.errorMessage);
}

/*Callback for lost connection*/
function ConnectionLost(res) {
	if (res.errorCode !== 0) {
		console.log("Connection lost:" + res.errorMessage);
		Connect();
	}
}

/*Callback for incoming message processing */
function MessageArrived(message) {
	var hoy = new Date();
	console.log(message.destinationName + " : " + message.payloadString);

	if (message.destinationName == "home/temperature/room1") {
		const value_on_table = document.getElementById('temperature_value_room1');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;

		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/temperature/room2") {
		const value_on_table = document.getElementById('temperature_value_room2');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;
			
		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/temperature/bathroom") {
		const value_on_table = document.getElementById('temperature_value_bathroom');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;
			
		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/temperature/kitchen") {
		const value_on_table = document.getElementById('temperature_value_kitchen');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;
			
		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/temperature/garden") {
		const value_on_table = document.getElementById('temperature_value_garden');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;
			
		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/temperature/livingroom") {
		const value_on_table = document.getElementById('temperature_value_livingroom');
		if (parseFloat(message.payloadString)) {
			value_on_table.innerHTML = `${message.payloadString}°C`;
			
		} else {
			value_on_table.innerHTML = message.payloadString;
		}
	}
}