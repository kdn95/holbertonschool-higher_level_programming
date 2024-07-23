let toggle_header = document.getElementById("toggle_header");
let header = document.querySelector("header");

toggle_header.onclick = toggleHeaderElemClass;

function toggleHeaderElemClass() {
    header.classList.toggle("red");
    header.classList.toggle("green");

}