let socket = io("ws://127.0.0.1:5000");

function action_room1(action) {
  console.log(action);
  update_status("home/air/room1", action);
  socket.emit("front-back-home-air-room1", action);
}

function action_room2(action) {
  console.log(action);
  update_status("home/air/room2", action);
  socket.emit("front-back-home-air-room2", action);
}

function action_kitchen(action) {
  console.log(action);
  update_status("home/air/kitchen", action);
  socket.emit("front-back-home-air-kitchen", action);
}

function action_bathroom(action) {
  console.log(action);
  update_status("home/air/bathroom", action);
  socket.emit("front-back-home-air-bathroom", action);
}

function action_garden(action) {
  console.log(action);
  update_status("home/air/garden", action);
  socket.emit("front-back-home-air-garden", action);
}

function action_livingroom(action) {
  console.log(action);
  update_status("home/air/livingroom", action);
  socket.emit("front-back-home-air-livingroom", action);
}

socket.on("connect", function () {
  console.log("Conected");
  get_status("home/air/room1", "front-back-home-air-room1");
  get_status("home/air/room2", "front-back-home-air-room2");
  get_status("home/air/bathroom", "front-back-home-air-bathroom");
  get_status("home/air/kitchen", "front-back-home-air-kitchen");
  get_status("home/air/garden", "front-back-home-air-garden");
  get_status("home/air/livingroom", "front-back-home-air-livingroom");
});

socket.on("disconnect", function () {
  console.log("Disconnect");
});

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
      console.log("ULTIMO VALOR", action["status"]);
      socket.emit(socket_to_emit, action["status"]);
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
