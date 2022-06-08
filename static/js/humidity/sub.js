//var hostname = "127.0.0.1";
var hostname = "34.94.79.113";
var port = 9091;
var clientId = "sub-humidity-";
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
	mqttClient.subscribe("home/humidity/room1");
	mqttClient.subscribe("home/humidity/room2");
	mqttClient.subscribe("home/humidity/bathroom");
	mqttClient.subscribe("home/humidity/livingroom");
	mqttClient.subscribe("home/humidity/kitchen");
	mqttClient.subscribe("home/humidity/garden");
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
	console.log(message.destinationName + " : " + message.payloadString);

	if (message.destinationName == "home/humidity/room1") {
		const value_on_table = document.getElementById('humidity_value_room1');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/humidity/room2") {
		const value_on_table = document.getElementById('humidity_value_room2');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/humidity/bathroom") {
		const value_on_table = document.getElementById('humidity_value_bathroom');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/humidity/kitchen") {
		const value_on_table = document.getElementById('humidity_value_kitchen');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/humidity/garden") {
		const value_on_table = document.getElementById('humidity_value_garden');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}

	if (message.destinationName == "home/humidity/livingroom") {
		const value_on_table = document.getElementById('humidity_value_livingroom');
		if( parseFloat( message.payloadString) ){
			value_on_table.innerHTML = `${message.payloadString}%`;
		}else{
			value_on_table.innerHTML = message.payloadString;
		}
	}
}