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
