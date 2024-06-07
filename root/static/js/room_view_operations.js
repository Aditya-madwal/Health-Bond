// join a chatroom :

function joinchatroomfunc(roomCode, buttonElement) {

    var url = `http://127.0.0.1:8000/main/joinchatroom/${roomCode}`;

    var btnid = buttonElement.id;
    buttonElement.innerText = "Leave";
    buttonElement.style.backgroundColor = "#ee4e4e";
    // buttonElement.onclick = function () { leavechatroomfunc(btnid, this); };

    // to avoid any error occurence due to multiple tapping, we disable the button onclick function until the success is recieved after ajax request.
    buttonElement.onclick = function () { }

    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            console.log("joined " + roomCode);
            buttonElement.onclick = function () { leavechatroomfunc(btnid, this); };
        },
        error: function (xhr, status, error) {
            alert('An error occured, Try reloading the page.')
        }
    });
}

// leave a chatroom :

function leavechatroomfunc(roomCode, buttonElement) {
    var url = `http://127.0.0.1:8000/main/leavechatroom/${roomCode}`;

    var btnid = buttonElement.id;
    buttonElement.innerText = "Join";
    buttonElement.style.backgroundColor = "#42bb12";
    // buttonElement.onclick = function () { joinchatroomfunc(btnid, this); };

    // to avoid any error occurence due to multiple tapping, we disable the button onclick function until the success is recieved after ajax request.
    buttonElement.onclick = function () { }

    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            console.log("left" + roomCode);
            buttonElement.onclick = function () { joinchatroomfunc(btnid, this); };
        },
        error: function (xhr, status, error) {
            alert('An error occured, Try reloading the page.')
        }
    });
}

// js operations :

let path = window.location.pathname;
let parts = path.split('/');
let roomid = parts[parts.length - 1];

function pop_list(name, buttonelement) {
    // alert('left');
    document.getElementById(name).style.display = 'none';
    buttonelement.onclick = function () { joinchatroomfunc(roomid, this); append_list(name, this) };
}

function append_list(name, buttonelement) {
    // alert('joined');
    document.getElementById('member_list').innerHTML += `<li class="user" id="${name}">
        <span class="username">${name}</span>
        <button class="view-button">
          <a href="/main/user/${name}">View</a>
        </button>
      </li>`;
    buttonelement.onclick = function () { joinchatroomfunc(roomid, this); pop_list(name, this) };
}
