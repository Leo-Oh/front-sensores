let socket = io("ws://127.0.0.1:5000")
const API_URL = "http://127.0.0.1:8000/api/status";


function get_status(topic,socket_to_emit){

  fetch(`${API_URL}/${topic}`, {
  method: "GET",
  headers: {
      "Content-Type": "application/json",
},
}).then((response) => response.json())
  .catch((error) => {
      console.error("Error:", error);
})
  .then((response) => {
        console.log("ultimo",response["status"])
        last_value_sensor(socket_to_emit, response["status"])
});
}

function last_value_sensor(socket_to_emit,status){
console.log(socket_to_emit,status)
socket.emit(socket_to_emit,status)
}


function update_status(topic, status, websocket_topic) {
socket.emit(websocket_topic,status)

let data = {
topic: topic,
status: status,
};
fetch(`${API_URL}/${topic}`, {
method: "PUT",
body: JSON.stringify(data),
headers: {
  "Content-Type": "application/json",
},
})
.then((response) => response.json())
.catch((error) => {
  console.error("Error:", error);
})
.then((response) => {
    console.log(response.topic);
    console.log("Estado del sensor actualizado");
  
});
}


function action_room1(action){
  console.log(action);
  update_status("home/temperature/room1", action,'front-back-home-temperature-room1')
}
    
function action_room2(action){
  console.log(action);
  update_status("home/temperature/room2", action, 'front-back-home-temperature-room2' )
}


function action_kitchen(action){
  console.log(action);
  update_status("home/temperature/kitchen", action,'front-back-home-temperature-kitchen')
}

function action_bathroom(action){
  console.log(action);
  update_status("home/temperature/bathroom", action, 'front-back-home-temperature-bathroom')
}

function action_garden(action){
  console.log(action);
  update_status("home/temperature/garden", action,'front-back-home-temperature-garden')
}

function action_livingroom(action){
  console.log(action);
  update_status("home/temperature/livingroom", action,'front-back-home-temperature-livingroom')
}

    


socket.on('connect', function(){
  console.log('Conected')
})

socket.on('disconnect', function(){
  console.log('Disconnect')
})
