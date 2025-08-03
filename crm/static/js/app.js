// /message timer for message notification
// var message_timeout = document.getElementById("message-timer");
// if (message_timeout) {
//     setTimeout(function () {
//         message_timeout.remove();
//     }, 2000);
// }
var message_timeout = document.getElementById("message-timer");
if (message_timeout) {
    message_timeout.addEventListener('transitionend', function() {
        message_timeout.remove();
    });
    message_timeout.classList.add('animate');
}




