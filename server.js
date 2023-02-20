import { io } from "socket.io-server";
const express = require("express");
const http = require("http");
const socketio = require("socket.io");

const app = express();

const PORT = process.env.PORT || 5000;

const server = http.createServer(app);

io = socketio(server);

io.on("connection", (socket) => {
   socket.on("join", ({ name }, callback) => {

    if (error) {
      callback(error);
    } else {
      let roomID = 2436
      socket.join(roomID)
      console.log(name)
       socket.broadcast.to(roomID).emit("adminMessage", {
             name: "admin",
             content: `${name} has joined`,
         });
      });

    socket.on("disconnect", () => {
         });
        });
})

server.listen(PORT, () => {
  console.log(`server running at port ${PORT}`);
});