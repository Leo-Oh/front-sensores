//var hostname = "127.0.0.1";
var hostname = "34.94.79.113";
var port = 9091;
var clientId = "sub-home-";
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

let variation_to_change = 0.001;
let temp_before_act_temp_r1 = 0;
let temp_before_act_temp_r2 = 0;
let temp_before_act_temp_liv2 = 0;

let temperatura_to_keep_room1 = 30;
let temperatura_to_keep_room2 = 30;
let temperatura_to_keep_kitchen = 20;

let temperatura_to_keep_livingroom = 30;

let total_active = 0;
let average_temperature = 0;
/*Callback for incoming message processing */
function MessageArrived(message) {
	console.log(message.destinationName + " : " + message.payloadString);

	if (message.destinationName == "home/temperature/room1")
		if (message.payloadString != "--" ) {
			new_temperature = parseFloat(message.payloadString)
			if ((new_temperature > (temp_before_act_temp_r1 + variation_to_change)) || (new_temperature < (temp_before_act_temp_r1 - variation_to_change)))
				temp_before_act_temp_r1 = new_temperature;
			if (temp_before_act_temp_r1 >= temperatura_to_keep_room1) {
				const value_average = document.getElementById('actuardor-clima-room1');
				value_average.innerHTML = `<div class="alert alert-success" role="alert">
                    	Clima room1: on
                 </div>`;
			} else {
				const value_average = document.getElementById('actuardor-clima-room1');
				value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
						Clima room1: off
                 	</div>`;
			}
		} else {
			const value_average = document.getElementById('actuardor-clima-room1');
			value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
			Clima room1: off
		 </div>`;
		}


	if (message.destinationName == "home/temperature/room2")
		if (message.payloadString != "--") {
			new_temperature = parseFloat(message.payloadString)
			if ((new_temperature > (temp_before_act_temp_r2 + variation_to_change)) || (new_temperature < (temp_before_act_temp_r2 - variation_to_change)))
				temp_before_act_temp_r2 = new_temperature;
			if (temp_before_act_temp_r2 >= temperatura_to_keep_room2) {
				console.log("VALOR ACTUAL DE ACTUADOR 2", temp_before_act_temp_r2)
				const value_average = document.getElementById('actuardor-clima-room2');
				value_average.innerHTML = `<div class="alert alert-success" role="alert">
					Clima room2: on
				 </div>`;
			} else {
				const value_average = document.getElementById('actuardor-clima-room2');
				value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
						Clima room2: off
                 	</div>`;
			}
		} else {
			const value_average = document.getElementById('actuardor-clima-room2');
			value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
			Clima room2: off
		 </div>`;
		}

	if (message.destinationName == "home/temperature/bathroom")
		average_temperature += parseFloat(message.payloadString)

	if (message.destinationName == "home/temperature/kitchen")
		average_temperature += parseFloat(message.payloadString)

	if (message.destinationName == "home/temperature/garden")
		average_temperature += parseFloat(message.payloadString)

	if (message.destinationName == "home/temperature/livingroom")
		if (average_temperature != "--") {
			new_temperature = parseFloat(message.payloadString)
			if ((new_temperature > (temp_before_act_temp_liv2 + variation_to_change)) || (new_temperature < (temp_before_act_temp_liv2 - variation_to_change)))
				temp_before_act_temp_liv2 = new_temperature;
			if (temp_before_act_temp_liv2 <= temperatura_to_keep_livingroom) {
				const value_average = document.getElementById('actuardor-calefactor-livingroom');
				value_average.innerHTML = `<div class="alert alert-success" role="alert">
					Calefactor livingroom: on
				 </div>`;
			} else {
				const value_average = document.getElementById('actuardor-calefactor-livingroom');
				value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
				Calefactor livingroom: off
			 </div>`;
			}
		} else {
			const value_average = document.getElementById('actuardor-calefactor-livingroom');
			value_average.innerHTML = `<div class="alert alert-secondary" role="alert">
			Calefactor livingroom: off
		 </div>`;
		}

	try {
		//console.log("total",average_temperature);
		average_temperature /= 6;
	} catch (e) {
		console.log(e);
	}

	console.log(average_temperature);
	if (average_temperature != "--") {
		const value_average = document.getElementById('averageTemperatureHome');
		value_average.innerHTML = `${average_temperature.toFixed(2)}°C`;
	} else {
		const value_average = document.getElementById('averageTemperatureHome');
		value_average.innerHTML = "--";
	}


	average_temperature = 0;
}



function setTemperature_room1() {

	Swal.fire({
		title: "Set tha temperature to keep in the room1",
		input: "text",
		inputAttributes: {
			autocapitalize: "off",
		},
		showCancelButton: true,
		confirmButtonText: "Find",
		showLoaderOnConfirm: true,
		preConfirm: (valor) => {
			if (parseFloat(valor)) {
				
				if((parseFloat(valor) >= 10) && ( parseFloat(valor) <= 40)){
					temperatura_to_keep_room1 = parseFloat(valor);
				}else{
					Swal.fire({
						icon: 'error',
						title: 'Oops...',
						text: 'Value out of range!',
						footer: 'The temperature should be between 10 and 40'
					})
				}
			} else {
				Swal.fire({
					icon: 'error',
					title: 'Oops...',
					text: 'You should insert a new value!',
					footer: 'The temperature should be between 10 and 40'
				})
			}
		},
		allowOutsideClick: () => !Swal.isLoading(),
	});
}



function setTemperature_room2() {

	Swal.fire({
		title: "Set tha temperature to keep in the room2",
		input: "text",
		inputAttributes: {
			autocapitalize: "off",
		},
		showCancelButton: true,
		confirmButtonText: "Find",
		showLoaderOnConfirm: true,
		preConfirm: (valor) => {
			if (parseFloat(valor)) {
				
				if((parseFloat(valor) >= 10) && ( parseFloat(valor) <= 40)){
					temperatura_to_keep_room2 = parseFloat(valor);
				}else{
					Swal.fire({
						icon: 'error',
						title: 'Oops...',
						text: 'Value out of range!',
						footer: 'The temperature should be between 10 and 40'
					})
				}
			} else {
				Swal.fire({
					icon: 'error',
					title: 'Oops...',
					text: 'You should insert a new value!',
					footer: 'The temperature should be between 10 and 40'
				})
			}
		},
		allowOutsideClick: () => !Swal.isLoading(),
	});
}


function setTemperature_livingroom() {

	Swal.fire({
		title: "Set tha temperature to keep in the livingroom",
		input: "text",
		inputAttributes: {
			autocapitalize: "off",
		},
		showCancelButton: true,
		confirmButtonText: "Find",
		showLoaderOnConfirm: true,
		preConfirm: (valor) => {
			if (parseFloat(valor)) {
				
				if((parseFloat(valor) >= 10) && ( parseFloat(valor) <= 40)){
					temperatura_to_keep_livingroom = parseFloat(valor);
				}else{
					Swal.fire({
						icon: 'error',
						title: 'Oops...',
						text: 'Value out of range!',
						footer: 'The temperature should be between 10 and 40'
					})
				}
			} else {
				Swal.fire({
					icon: 'error',
					title: 'Oops...',
					text: 'You should insert a new value!',
					footer: 'The temperature should be between 10 and 40'
				})
			}
		},
		allowOutsideClick: () => !Swal.isLoading(),
	});
}
