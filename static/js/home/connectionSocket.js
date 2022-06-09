let socket = io("ws://0.0.0.0:9096");

socket.on('connect', function(){
    console.log('Conected')
})

socket.on('disconnect', function(){
    console.log('Disconnect')
})

function action_all(action){
  console.log(action);
  socket.emit('front-back-home',action);
}


    


