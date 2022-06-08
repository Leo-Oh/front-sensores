let socket = io("ws://127.0.0.1:5000")
const API_URL = "http://127.0.0.1:8000/api/status";


function action_room1(action){
  update_status("home/temperature/room1", action)
  
  //ssocket.emit('front-back-home-temperature-room1',action)
}
    
function action_room2(action){
  console.log(action);
  update_status("home/temperature/room2", action)
  socket.emit('front-back-home-temperature-room2',action)
}


function action_kitchen(action){
  console.log(action);
  update_status("home/temperature/kitchen", action)
  socket.emit('front-back-home-temperature-kitchen',action)
}

function action_bathroom(action){
  console.log(action);
  update_status("home/temperature/bathroom", action)
  socket.emit('front-back-home-temperature-bathroom',action)
}

function action_garden(action){
  console.log(action);
  update_status("home/temperature/garden", action)
  socket.emit('front-back-home-temperature-garden',action)
}

function action_livingroom(action){
  console.log(action);
  update_status("home/temperature/livingroom", action)
  socket.emit('front-back-home-temperature-livingroom',action)
}


    socket.on('connect', function(){
        console.log('Conected')

        get_status("home/temperature/room1", "front-back-home-temperature-room1")
        get_status("home/temperature/room2", "front-back-home-temperature-room2")
        get_status("home/temperature/bathroom", "front-back-home-temperature-bathroom")
        get_status("home/temperature/kitchen", "front-back-home-temperature-kitchen")
        get_status("home/temperature/garden", "front-back-home-temperature-garden")
        get_status("home/temperature/livingroom", "front-back-home-temperature-livingroom")
        
    })

    socket.on('disconnect', function(){
        console.log('Disconnect')
    })


    
function get_status(topic, socket_to_emit){
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
          if(response["topic"] === "home/temperature/room1" ){
            sensor_status[topic] = response["status"]
            socket.emit(socket_to_emit,sensor_status[topic])
          }
          
 
    });
}

function update_status(topic, status) {
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
      if (response.status === 200) {
        console.log("Estado del sensor actualizado");
      }
    });
}
