// use getElementById = red_header
let red_header = document.getElementById("red_header");
// when header is on click, expect to change color
red_header.onclick = changeColourToRed;

function changeColourToRed() {
    red_header.style.color = 'red';
}