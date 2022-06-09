let socket = io("ws://127.0.0.1:9096");

socket.on('connect', function(){
  console.log('Conected')
})

socket.on('disconnect', function(){
  console.log('Disconnect')
})

function action_room1(action){
  console.log(action);
  update_status("home/air/room1", action,'front-back-home-air-room1')
}
    
function action_room2(action){
  console.log(action);
  update_status("home/air/room2", action, 'front-back-home-air-room2' )
}


function action_kitchen(action){
  console.log(action);
  update_status("home/air/kitchen", action,'front-back-home-air-kitchen')
}

function action_bathroom(action){
  console.log(action);
  update_status("home/air/bathroom", action, 'front-back-home-air-bathroom')
}

function action_garden(action){
  console.log(action);
  update_status("home/air/garden", action,'front-back-home-air-garden')
}

function action_livingroom(action){
  console.log(action);
  update_status("home/air/livingroom", action,'front-back-home-air-livingroom')
}
    
function get_status(topic,socket_to_emit){

  let sensor_status = null;
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
          //console.log("ultimo",response["status"])
          last_value_sensor(socket_to_emit, response["status"])
  });
}

function last_value_sensor(socket_to_emit,status){
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
   
      console.log("Estado del sensor actualizado");
    
  });
}
