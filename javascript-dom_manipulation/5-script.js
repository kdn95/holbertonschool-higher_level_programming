let update_header = document.getElementById("update_header");
let header = document.querySelector("header");

update_header.onclick = swapHeaderText;

function swapHeaderText() {
    header.textContent = "New Header!!!";
}