// websocket work of the chatroom

// getting the roomcode :
let url = window.location.href;
let urlParts = url.split('/');
let roomcode = urlParts[urlParts.length - 1];

console.log(roomcode);

// getting the user's username :
let currentUser = document.getElementById("current-user").value;
console.log("Current user:", currentUser);

// contrcuting the websocket :

let websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
let wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/notification/${roomcode}/`;
let socket = new WebSocket(wsEndpoint);

socket.onopen = (event) => {
    console.log("WebSocket connection opened!");
};

socket.onclose = (event) => {
    console.log("WebSocket connection closed!");
};

// socket.onmessage = function (event) {
//     let message = JSON.parse(event.data); // Parse received data (assuming JSON format)
//     alert("message recieved")
//     // Process the received message (e.g., update UI, trigger actions)
// };

// sending the msg to socket on some particular event:

document.getElementById('msg_send_form').addEventListener('submit', function (event) {
    let formElement = document.getElementById("msg_send_form");
    let textareaValue = formElement.querySelector("textarea").value;
    event.preventDefault();
    let message = textareaValue;
    socket.send(
        JSON.stringify({
            'message': message,
            'room_code': roomcode,
            'sender_username': currentUser,
        })
    );
    console.log(message);
    formElement.querySelector("textarea").value = "";
});


socket.addEventListener("message", (event) => {
    // here event is : {isTrusted: true, data: '{"message": {"sender": "test_user_1_health", "message": "dkewnfkewn"}}', origin: 'ws://127.0.0.1:8000', lastEventId: '', source: null, …}
    let message_data = JSON.parse(event.data)['message']
    console.log(message_data)
    let sender = message_data['sender']
    let content = message_data['message']
    let roomcode = message_data['roomcode']
    if (sender === currentUser) {
        document.getElementById('chats').innerHTML += `<br /><div class="message sent-by-me">
        <div class="message-sender">You</div>
        <div class="message-content">${content}</div>
        <div class="message-timestamp">${getFormattedDateTime()}</div>
    </div>`
    } else {
        document.getElementById('chats').innerHTML += `<br/><div class="message received">
        <div class="message-sender">${sender}</div>
        <div class="message-content">${content}</div>
        <div class="message-timestamp">${getFormattedDateTime()}</div>
      </div>`
    }
    scrollToBottom("scrollable-div");
})


function getFormattedDateTime() {
    let today = new Date();
    let month = today.toLocaleString('default', { month: 'long' });
    let day = today.getDate();
    let year = today.getFullYear();
    let hours = today.getHours();
    let minutes = today.getMinutes();
    let amPm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12;
    let formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}${amPm}`;
    let fullDate = `${month} ${day}, ${year}, ${formattedTime}`;
    return fullDate;
}

// scroll to bottom automatically :

function scrollToBottom(elementId) {
    var element = document.getElementById(elementId);
    if (element) {
        element.scrollTop = element.scrollHeight;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    scrollToBottom("scrollable-div");
});


// chatroom hideable :
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('hidden');
}

document.querySelector("textarea").placeholder = "Enter some message...";

document.addEventListener('keydown', function (event) {
    if (event.ctrlKey && event.key === 'b') {
        event.preventDefault();  // Prevent the default browser action for Ctrl+B
        toggleSidebar();
    }
});
