let header = document.querySelector("header");
let red_header = document.getElementById("red_header");

red_header.onclick = addRedClassToHeaderTag;

function addRedClassToHeaderTag() {
    header.classList.add("red");
}