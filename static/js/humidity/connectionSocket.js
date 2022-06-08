let socket = io("ws://127.0.0.1:5000")


function action_room1(action) {
  console.log(action);
  update_status("home/humidity/room1", action)
  socket.emit('front-back-home-humidity-room1', action)
}

function action_room2(action) {
  console.log(action);
  update_status("home/humidity/room2", action)
  socket.emit('front-back-home-humidity-room2', action)
}


function action_kitchen(action) {
  console.log(action);
  update_status("home/humidity/kitchen", action)
  socket.emit('front-back-home-humidity-kitchen', action)
}

function action_bathroom(action) {
  console.log(action);
  update_status("home/humidity/bathroom", action)
  socket.emit('front-back-home-humidity-bathroom', action)
}

function action_garden(action) {
  console.log(action);
  update_status("home/humidity/garden", action)
  socket.emit('front-back-home-humidity-garden', action)
}

function action_livingroom(action) {
  console.log(action);
  update_status("home/humidity/livingroom", action)
  socket.emit('front-back-home-humidity-livingroom', action)
}

socket.on('connect', function () {
  console.log('Conected')
  get_status("home/humidity/room1", "front-back-home-humidity-room1")
  get_status("home/humidity/room2", "front-back-home-humidity-room2")
  get_status("home/humidity/bathroom", "front-back-home-humidity-bathroom")
  get_status("home/humidity/kitchen", "front-back-home-humidity-kitchen")
  get_status("home/humidity/garden", "front-back-home-humidity-garden")
  get_status("home/humidity/livingroom", "front-back-home-humidity-livingroom")

})

socket.on('disconnect', function () {
  console.log('Disconnect')
})



function get_status(topic, socket_to_emit) {
  fetch(`${API_URL}/${topic}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    })
    .then((action) => {
      console.log("ULTIMO VALOR", action["status"])
      socket.emit(socket_to_emit, action["status"])
    });
}

function update_status(topic, status) {
  console.log(topic, status);
  console.log(`${API_URL}/${topic}`)
  let data = {
    topic: topic,
    status: parseInt(status),
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
