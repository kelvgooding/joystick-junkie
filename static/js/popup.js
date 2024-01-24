// script.js
var buttons = document.querySelectorAll('.game-image');
var closeButtons = document.querySelectorAll('.closePopup');

buttons.forEach(function (button, index) {
    button.addEventListener("click", function () {
        document.getElementById('myPopup' + (index + 1)).classList.add("show");
    });
});

closeButtons.forEach(function (closeButton, index) {
    closeButton.addEventListener("click", function () {
        document.getElementById('myPopup' + (index + 1)).classList.remove("show");
    });
});

window.addEventListener("click", function (event) {
    closeButtons.forEach(function (closeButton, index) {
        var popup = document.getElementById('myPopup' + (index + 1));
        if (event.target == popup) {
            popup.classList.remove("show");
        }
    });
});
